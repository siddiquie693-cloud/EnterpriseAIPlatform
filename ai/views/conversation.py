from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

from ai.models import Conversation
from ai.serializers import ConversationSerializer

class ConversationListAPIView(generics.ListAPIView):
    """
    List all conversations of the logged-in user.
    Supports search by title.
    """

    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)
    
class ConversationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, rename and delete a conversation.
    """

    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Conversation.objects.filter(
            user=self.request.user
        )    