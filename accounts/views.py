from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import update_session_auth_hash
from .serializers import UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import (
    UserRegistrationSerializer,
    ChangePasswordSerializer,
    LogoutSerializer,
)

from drf_spectacular.utils import (
    extend_schema,
    OpenApiExample,
    OpenApiResponse,
)

@extend_schema(
    tags=["Authentication"],
    summary="Register User",
    description="Create a new user account.",
    request=UserRegistrationSerializer,
    responses={
        201: OpenApiResponse(description="User registered successfully."),
        400: OpenApiResponse(description="Validation failed."),
    },
    examples=[
        OpenApiExample(
            "Register",
            value={
                "username": "john",
                "email": "john@example.com",
                "password": "Password@123",
                "password2": "Password@123",
            },
            request_only=True,
        )
    ],
)

class RegisterAPIView(APIView):
    """
    API for user registration.
    """

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "status": "success",
                    "message": "User registered successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "status": "error",
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
@extend_schema(
    tags=["Authentication"],
    summary="Change Password",
    description="Change the authenticated user's password.",
    request=ChangePasswordSerializer,
    responses={
        200: OpenApiResponse(description="Password changed successfully."),
        400: OpenApiResponse(description="Validation failed."),
    },
)

class ChangePasswordAPIView(APIView):
    """
    API for changing the authenticated user's password.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            user = request.user
            if not user.check_password(
                serializer.validated_data["old_password"]
            ):
                return Response(
                    {
                        "status": "error",
                        "message": "Old password is incorrect.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user.set_password(
                serializer.validated_data["new_password"]
            )
            user.save()
            update_session_auth_hash(request, user)
            return Response(
                {
                    "status": "success",
                    "message": "Password changed successfully.",
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "status": "error",
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
@extend_schema(
    tags=["Authentication"],
    summary="Logout",
    description="Blacklist the refresh token and logout the current user.",
    request=LogoutSerializer,
    responses={
        200: OpenApiResponse(description="Logout successful."),
        400: OpenApiResponse(description="Invalid refresh token."),
    },
)
    
class LogoutAPIView(APIView):
    """
    API for logging out a user.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "status": "success",
                    "message": "Logout successful."
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "status": "error",
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )    