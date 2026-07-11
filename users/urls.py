from django.urls import path
from .views import (
    UserProfileAPIView,
    AssignGroupAPIView,
    UserListAPIView,
    UserDetailAPIView,
    UserUpdateAPIView,
    UserStatusAPIView,
)

urlpatterns = [
    path("profile/", UserProfileAPIView.as_view(), name="profile",),
    path("assign-group/", AssignGroupAPIView.as_view(), name="assign_group",),
    path("", UserListAPIView.as_view(), name="user-list",),
    path("<int:pk>/", UserDetailAPIView.as_view(), name="user-detail",),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user-update",),
    path("<int:pk>/status/", UserStatusAPIView.as_view(), name="user-status"),
]