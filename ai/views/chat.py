from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ai.serializers import ChatSerializer
from ai.services.llm_service import LLMService
from ai.services.rag_service import RAGService

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

        rag_service = RAGService()

        result = rag_service.answer_question(prompt)

        return Response(
            result,
            status=status.HTTP_200_OK,
        )