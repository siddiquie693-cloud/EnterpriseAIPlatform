from rest_framework import serializers
from ai.models import Conversation, Message

class ChatSerializer(serializers.Serializer):
    """
    Serializer for AI chat requests.
    """
    prompt = serializers.CharField()

class QuestionSerializer(serializers.Serializer):
    question = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
    )

class ConversationSerializer(serializers.ModelSerializer):
    """
    Serializer for conversations.
    """

    class Meta:
        model = Conversation
        fields = (
            "id",
            "title",
            "created_at",
            "updated_at",
        )

class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for chat messages.
    """

    class Meta:
        model = Message
        fields = (
            "id",
            "role",
            "content",
            "created_at",
        )                