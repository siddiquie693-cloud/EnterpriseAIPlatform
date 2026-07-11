from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from documents.mixins import DocumentQuerysetMixin
from documents.serializers import DocumentUpdateSerializer

class DocumentUpdateAPIView(
    DocumentQuerysetMixin,
    generics.UpdateAPIView,
):
    """
    Update document metadata.
    """
    serializer_class = DocumentUpdateSerializer
    permission_classes = [IsAuthenticated]

    