from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ai.serializers import ChatSerializer
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
            conversation = Conversation.objects.create(
                user=request.user,
                title=prompt[:100],
            )      

        # Save user message
        Message.objects.create(
            conversation=conversation,
            role="user",
            content=prompt,
        )    

        rag_service = RAGService()

        result = rag_service.answer_question(
            question=prompt, 
            document_id=document_id,
            conversation_id=conversation.id,
        )

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