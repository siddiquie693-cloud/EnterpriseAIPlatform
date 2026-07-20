from django.contrib.auth import get_user_model
from rest_framework import generics, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ( 
    UserProfileSerializer,
    AssignGroupSerializer,
    UserUpdateSerializer,
    UserStatusSerializer,
)
from drf_spectacular.utils import extend_schema
from .permissions import IsAdmin

User = get_user_model()

class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    """
    Retrieve and update the authenticated user's profile.
    """

    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
@extend_schema(
    request=AssignGroupSerializer,
    responses={200: dict},
)

class AssignGroupAPIView(APIView):
    """
    Assign a user to a group.
    """
    permission_classes = [IsAdmin]
    serializer_class = AssignGroupSerializer

    def post(self, request):
        serializer = AssignGroupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "status": "success",
                    "message": "Group assigned successfully.",
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
            
class UserListAPIView(generics.ListAPIView):
    """
    List all users.
    """
    queryset = User.objects.all().order_by("id")
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdmin]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "username",
        "email",
        "first_name",
        "last_name",
    ]

    filterset_fields = [
        "is_active",
    ]

    ordering_fields = [
        "id",
        "username",
        "email",
    ]

    ordering = ["id"]

class UserDetailAPIView(generics.RetrieveAPIView):
    """
    Retrieve details of a specific user.
    """
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdmin]

class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Update a user's information.
    """
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAdmin]

class UserStatusAPIView(generics.UpdateAPIView):
    """
    Activate or deactivate a user.
    """
    queryset = User.objects.all()
    serializer_class = UserStatusSerializer
    permission_classes = [IsAdmin]