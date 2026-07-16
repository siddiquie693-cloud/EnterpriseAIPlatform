from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ai.serializers import QuestionSerializer
from documents.models import Document
from ai.services.rag_service import RAGService

class AskQuestionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, document_id):
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            document = Document.objects.get(
                id=document_id,
                uploaded_by=request.user,
            )
        except Document.DoesNotExist:
            return Response(
                {"detail": "Document not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        rag_service = RAGService()

        result = rag_service.answer_question(
            question=serializer.validated_data["question"],
            document_id=document_id,
        )

        return Response(result)