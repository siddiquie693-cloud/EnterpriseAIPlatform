from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ai.models import Conversation
from ai.serializers import ConversationSerializer

class ConversationListAPIView(generics.ListAPIView):
    """
    List all conversations of the logged-in user.
    """

    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)
    
class ConversationDetailAPIView(generics.RetrieveAPIView):
    """
    Retrieve a single conversation with all messages.
    """

    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Conversation.objects.filter(
            user=self.request.user
        )    