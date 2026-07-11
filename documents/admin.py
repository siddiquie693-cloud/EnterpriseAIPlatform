from django.contrib import admin
from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """
    Admin configuration for document model.
    """

    list_display = (
        "id",
        "title",
        "uploaded_by",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
        "uploaded_by_username",
    )

    ordering = (
        "-created_at",
    )
