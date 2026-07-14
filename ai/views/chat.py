from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ai.serializers import ChatSerializer
from ai.services.llm_service import LLMService
from ai.services.rag_service import RAGService
from ai.models import Conversation, Message

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

        # Optional document ID
        document_id = request.data.get("document_id")

        if document_id:
            document_id = int(document_id)

        # Create a new conversation
        conversation = Conversation.objects.create(
            user=request.user,
            title=prompt[:50],
        )

        # Save user message
        Message.objects.create(
            conversation=conversation,
            role="user",
            content=prompt,
        )    

        rag_service = RAGService()

        result = rag_service.answer_question(question=prompt, document_id=document_id,)

        # Save AI response 
        Message.objects.create(
            conversation=conversation,
            role="assistant",
            content=result["answer"],
        )
        result["conversation_id"] = conversation.id

        return Response(
            result,
            status=status.HTTP_200_OK,
        )