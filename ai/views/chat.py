from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ai.serializers import ChatSerializer
from ai.services.llm_service import LLMService

class ChatAPIView(APIView):
    """
    AI chat endpoint.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChatSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        prompt = serializer.validated_data["prompt"]

        answer = LLMService.chat(prompt)

        return Response(
            {
                "status": "success",
                "response": answer,
            },
            status=status.HTTP_200_OK,
        )