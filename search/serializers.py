from rest_framework import serializers

class SearchSerializer(serializers.Serializer):
    """
    Validate Hybrid Search request.
    """

    query = serializers.CharField(
        required=True,
        max_length=500,
    )

    document_id = serializers.IntegerField(
        required=False,
        allow_null=True,
    )

    top_k = serializers.IntegerField(
        required=False,
        default=5,
        min_value=1,
        max_value=20,
    )