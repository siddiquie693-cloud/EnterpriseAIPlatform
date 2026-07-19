import logging
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import StreamingHttpResponse

from ai.serializers import ChatSerializer
from ai.services.workflow import workflow
from ai.models import Conversation, Message
from ai.services.llm_service import LLMService

from drf_spectacular.utils import (
    extend_schema,
    OpenApiExample,
    OpenApiResponse,
)

logger = logging.getLogger("enterprise_ai")

@extend_schema(
    tags=["AI Chat"],
    summary="Chat with Enterprise AI Assistant",
    description="""
Interact with the Enterprise AI Assistant using Retrieval-Augmented Generation (RAG),
LangGraph workflow, conversation memory, and citations.

Features:
- Document-aware responses
- Conversation memory
- AI-generated summaries
- Source citations
- Multi-turn conversations
""",
   request=ChatSerializer,
   responses={
       200: OpenApiResponse(
           description="AI response generated successfully."
       ),
       400: OpenApiResponse(
           description="Invalid request."
       ),
       404: OpenApiResponse(
           description="Conversation not found."
       ),
       500: OpenApiResponse(
           description="Internal server error."
       ),
   },
   examples=[
       OpenApiExample(
           "New Conversation",
           value={
               "prompt": "What is Artificial Intelligence?"
           },
           request_only=True,
       ),
       OpenApiExample(
           "Continue Conversation",
           value={
               "prompt": "give another example",
               "conversation_id": 26
           },
           request_only=True,
       ),
   ],

)

class ChatAPIView(APIView):
    """
    Chat with index document using RAG.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChatSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        prompt = serializer.validated_data["prompt"]

        logger.info(
            f"Chat request received | User={request.user.id} | Prompt={prompt}"
        )

        # Optional document ID
        document_id = request.data.get("document_id")

        if document_id:
            document_id = int(document_id)

        # Optional conversation ID 
        conversation_id = request.data.get("conversation_id")

        conversation = None

        if conversation_id:
            try:
                conversation = Conversation.objects.get(
                    id=conversation_id,
                    user=request.user,
                )
            except Conversation.DoesNotExist:
                return Response(
                    {
                        "error": "Conversation not found."
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            # Generate AI title 
            try:
                title = LLMService.generate_title(prompt)
            except Exception:
                # Fallback if title generation fails 
                title = prompt[:100]

            conversation = Conversation.objects.create(
                user=request.user,
                title=title,
            )

            logger.info(
                f"conversation created | ID={conversation.id}"
            )      

        # Save user message
        Message.objects.create(
            conversation=conversation,
            role="user",
            content=prompt,
        )    

        state = {
            "question": prompt,
            "document_id": document_id,
            "context": [],
            "research": "",
            "summary": "",
            "answer": "",
            "conversation_id": conversation.id,
            "conversation_history": "",
        }

        try:
            logger.info("Starting LangGraph workflow...")
            
            state = workflow.invoke(state)

            logger.info("LangGraph workflow completed.")
        except Exception:
            logger.exception("LangGraph workflow failed")

            return Response(
                {
                    "error": "Somethiing went wrong while generating the response."
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )    

        result = {
            "question": prompt,
            "answer": state["answer"],
            "summary": state["summary"],
            "research": state["research"],
            "context": state["context"],
            "sources": list(
                {
                    item["document_id"]
                    for item in state["context"]
                }
            ),
            "citations": state["context"],
            "conversation_id": conversation.id,
        }

        # Save AI response 
        Message.objects.create(
            conversation=conversation,
            role="assistant",
            content=result["answer"],
        )

        logger.info(
            f"Response generated | Conversation={conversation.id}"
        )
        
        return Response(
            result,
            status=status.HTTP_200_OK,
        )
    
class StreamingChatAPIView(APIView):
    """
    Stream AI response in real time.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        prompt = request.data.get("prompt")

        if not prompt:
            return Response(
                {"error": "Prompt is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return StreamingHttpResponse(
            LLMService.stream_chat(prompt),
            content_type="text/plain",
        )    