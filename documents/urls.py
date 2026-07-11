from django.urls import path
from .views import ( 
    DocumentUploadAPIView,
    DocumentListAPIView,
    DocumentDetailAPIView,
    DocumentUpdateAPIView,
    DocumentStatusAPIView,
)

urlpatterns = [
    path("upload/", DocumentUploadAPIView.as_view(), name="document-upload",),
    path("", DocumentListAPIView.as_view(), name="document-list",),
    path("<int:pk>/", DocumentDetailAPIView.as_view(), name="document-detail",),
    path("<int:pk>/update/", DocumentUpdateAPIView.as_view(), name="document-update"),
    path("<int:pk>/status/", DocumentStatusAPIView.as_view(), name="document-status"),
]