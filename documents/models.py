from django.conf import settings
from django.db import models
import os

class Document(models.Model):
    """
    Stores uploaded documents.
    """

    FILE_TYPES = (
        ("pdf", "PDF"),
        ("docx", "DOCX"),
        ("txt", "TXT"),
    )

    title = models.CharField(max_length=255)
    file = models.FileField(
        upload_to="documents/",
    )

    # NEW
    file_type = models.CharField(
        max_length=10,
        choices=FILE_TYPES,
        blank=True,
    )


    description = models.TextField(
        blank=True,
    )

    summary = models.TextField(
        blank=True,
        default="",
    )

    is_summarized = models.BooleanField(
        default=False,
    )

    # NEW 
    processed = models.BooleanField(
        default=False,
    )

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="documents",
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        """
        Automatically detect file type.
        """
        if self.file:
            extension = os.path.splitext(self.file.name)[1].lower()

            if extension == ".pdf":
                self.file_type = "pdf"
            elif extension == ".docx":
                self.file_type = "docx"
            elif extension == ".txt":
                self.file_type = "txt"

        super().save(*args, **kwargs)                    

    def __str__(self):
        
        return self.title    