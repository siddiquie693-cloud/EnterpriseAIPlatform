from django.conf import settings
from django.db import models

class Document(models.Model):
    """
    Stores uploaded documents.
    """

    title = models.CharField(max_length=255)
    file = models.FileField(
        upload_to="documents/",
    )


    description = models.TextField(
        blank=True,
    )

    summary = models.TextField(
        blank=True,
        default=""
    )

    is_summarized = models.BooleanField(
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

    def __str__(self):
        return self.title    