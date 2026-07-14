from django.db import models
from django.conf import settings


class Conversation(models.Model):
    """
    Stores a conversation between a user and the AI.
    """

    title = models.CharField(max_length=255, default="New Conversation",)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="conversations",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title
class Message(models.Model):
    """
    Store individual chat messages.
    """

    ROLE_CHOICES = (
        ("user", "User"),
        ("assistant", "Assistant"),
    ) 

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages",
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.role}: {self.content[:50]}"         
