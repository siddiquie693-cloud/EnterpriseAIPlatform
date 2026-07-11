from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    """
    Serializer for document upload and retrieval.
    """
    class Meta:
        model = Document
        fields = (
            "id",
            "title",
            "description",
            "file",
            "uploaded_by",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "uploaded_by",
            "created_at",
            "updated_at",
        )

class DocumentUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating document metadata.
    """

    class Meta:
        model = Document
        fields = (
            "title",
            "description",
        )

class DocumentStatusSerializer(serializers.ModelSerializer):
    """
    Serializer for activating/deactivating a document.
    """
    class Meta:
        model = Document
        fields = ("is_active",)

