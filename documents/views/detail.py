from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from documents.mixins import DocumentQuerysetMixin
from documents.serializers import DocumentSerializer

class DocumentDetailAPIView(
    DocumentQuerysetMixin,
    generics.RetrieveAPIView,
):
    
    """
    Retrieve a single document.
    """
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    