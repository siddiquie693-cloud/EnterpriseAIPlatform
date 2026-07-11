from rest_framework import serializers

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