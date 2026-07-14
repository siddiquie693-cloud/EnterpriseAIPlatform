from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ai.services.document_index_service import DocumentIndexService
from documents.models import Document
from documents.serializers import DocumentSerializer

class DocumentUploadAPIView(generics.CreateAPIView):
    """
    Upload a new document.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
       document = serializer.save(uploaded_by=self.request.user)
       DocumentIndexService().index_document(document)
