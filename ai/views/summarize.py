from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from documents.models import Document

from ai.services.document_service import DocumentService
from ai.services.llm_service import LLMService

class SummarizeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, document_id):
        try:
            document = Document.objects.get(
                id=document_id,
                uploaded_by=request.user,
            )
        except Document.DoesNotExist:
            return Response(
                {"detail": "document not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        # Return cached summary if it already exist
        if document.is_summarized:
            return Response(
                {
                    "status": "success",
                    "summary": document.summary,
                    "cached": True,
                }
            )
        
        # Extract document text
        text = DocumentService.extract_text(document.file.path)

        # Generate AI summary
        summary = LLMService.summarize(text)

        # Save summary in DB
        document.summary = summary
        document.is_summarized = True
        document.save()

        return Response(
            {
                "status": "success",
                "summary": summary,
                "cached": False,
            }
        )    