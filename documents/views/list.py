from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.permissions import IsAuthenticated

from documents.mixins import DocumentQuerysetMixin
from documents.serializers import DocumentSerializer

class DocumentListAPIView(
    DocumentQuerysetMixin,
    generics.ListAPIView,
):
    """
    List documents based oon the user's role.
    """
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "is_active",
    ]

    search_fields = [
        "title",
        "description",
    ]

    ordering_fields = [
        "created_at",
        "updated_at",
        "title",
    ]

    ordering = [
        "-created_at",
    ]

    