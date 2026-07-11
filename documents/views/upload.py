from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from documents.models import Document
from documents.serializers import DocumentSerializer

class DocumentUploadAPIView(generics.CreateAPIView):
    """
    Upload a new document.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_class = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)