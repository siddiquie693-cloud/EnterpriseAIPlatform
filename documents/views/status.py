from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from documents.mixins import DocumentQuerysetMixin
from documents.serializers import DocumentStatusSerializer

class DocumentStatusAPIView(
    DocumentQuerysetMixin,
    generics.UpdateAPIView,
):
    """
    Activate or deactivate a document.
    """
    include_inactive = True

    serializer_class = DocumentStatusSerializer
    permission_classes = [IsAuthenticated]

    