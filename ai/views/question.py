from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ai.serializers import QuestionSerializer
from ai.services.document_service import DocumentService
from ai.services.llm_service import LLMService
from documents.models import Document
from ai.services.chunking_service import ChunkingService

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
        text = DocumentService.extract_text(document.file.path)
        chunks = ChunkingService.split_text(text)
        document_text = "\n\n".join(chunks)

        answer = LLMService.answer_question(
            document=document_text,
            question=serializer.validated_data["question"],
        ) 

        return Response(
            {
                "status": "success",
                "question": serializer.validated_data["question"],
                "answer": answer,
            }
        )  