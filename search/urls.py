from django.urls import path
from search.views import HybridSearchAPIView

urlpatterns = [
    path("", HybridSearchAPIView.as_view(), name="hybrid-search",),
]