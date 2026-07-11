from django.urls import path
from ai.views import (
     ChatAPIView, 
     SummarizeAPIView,
     AskQuestionAPIView,
)

urlpatterns = [
    path("chat/", ChatAPIView.as_view(), name="ai-chat",),
    path("summarize/<int:document_id>/", SummarizeAPIView.as_view(), name="summarize",),
    path("ask/<int:document_id>/", AskQuestionAPIView.as_view(), name="ask-question",),

]