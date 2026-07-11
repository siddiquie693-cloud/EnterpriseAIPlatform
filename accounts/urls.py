from django.urls import path
from .views import (
    RegisterAPIView,
    ChangePasswordAPIView,
    LogoutAPIView,
)

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register",),
    path("change-password/", ChangePasswordAPIView.as_view(), name="change_password",),
    path("logout/", LogoutAPIView.as_view(), name="logout",),
]