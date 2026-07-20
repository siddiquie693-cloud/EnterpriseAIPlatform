import json

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from documents.models import Document
from ai.chains.summarize_chain import summary_chain

from ai.services.document_service import DocumentService
from ai.services.llm_service import LLMService

from drf_spectacular.utils import extend_schema
from ai.serializers import DocumentSummarySerializer

@extend_schema(
    request=DocumentSummarySerializer,
    responses={200: dict},
)

class SummarizeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentSummarySerializer

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
        if document.is_summarized and document.summary:
            try:

                cached_summary = json.loads(document.summary)
                return Response(
                    {
                        "status": "success",
                        "title": document.title,
                        "executive_summary": cached_summary.get("executive_summary"),
                        "bullet_summary": cached_summary.get("bullet_summary"),
                        "key_topics": cached_summary.get("key_topics"),
                        "keywords": cached_summary.get("keywords"),
                        "important_questions": cached_summary.get("important_questions"),
                        "difficulty": cached_summary.get("difficulty"),
                        "estimated_reading_time": cached_summary.get("estimated_reading_time"),
                        "cached": True,
                    }
                )
            except json.JSONDecoderError:
                # Old summaries were stored as plain text.
                # Regenerate using the new structured prompt.
                pass   
        
        # Extract document text
        text = DocumentService.extract_text(document.file.path)

        # Generate AI summary
        summary = summary_chain.invoke(
            {
                "document": text,
            }
        )

        # Save structured summary

        document.summary = json.dumps(summary)
        document.is_summarized = True
        document.save()

        return Response(
            {
                "status": "success",
                "title": document.title,
                "executive_summary": summary.get("executive_summary"),
                "bullet_summary": summary.get("bullet_summary"),
                "key_topics": summary.get("key_topics"),
                "keywords": summary.get("keywords"),
                "important_questions": summary.get("important_questions"),
                "difficulty": summary.get("difficulty"),
                "estimated_reading_time": summary.get("estimated_reading_time"),
                "cached": False,
            }
        )

