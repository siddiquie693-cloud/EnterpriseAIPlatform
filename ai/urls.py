from django.urls import path
from ai.views import (
     ChatAPIView,
     StreamingChatAPIView, 
     SummarizeAPIView,
     AskQuestionAPIView,
     ConversationListAPIView,
     ConversationDetailAPIView,
    
)

urlpatterns = [
    path("chat/", ChatAPIView.as_view(), name="ai-chat",),
    path("summarize/<int:document_id>/", SummarizeAPIView.as_view(), name="summarize",),
    path("ask/<int:document_id>/", AskQuestionAPIView.as_view(), name="ask-question",),
    path("conversations/", ConversationListAPIView.as_view(), name="conversation-list",),
    path("conversations/<int:pk>/", ConversationDetailAPIView.as_view(), name="conversation-detail",),
    path("chat/stream/", StreamingChatAPIView.as_view(), name="ai-chat-stream",),

]