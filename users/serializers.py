from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import Group

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for authenticated user's profile.
    """

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        )
        read_only_fields = (
            "id",
            "username",
            "email",
        )

class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating user information by an admin.
    """
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "is_active",
        )

class UserStatusSerializer(serializers.ModelSerializer):
    """
    Serializer for activating/deactivating a user.
    """
    class Meta:
        model = User
        fields = (
            "is_active",
        )
        
class AssignGroupSerializer(serializers.Serializer):
    """
    Serializer for assigning a user to a group.
    """
    user_id = serializers.IntegerField()
    group = serializers.CharField(max_length=50)

    def validate(self, attrs):
        user_id = attrs.get("user_id")
        group_name = attrs.get("group")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({"user_id": "User does not exist."})

        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            raise serializers.ValidationError({"group": "Group does not exist."})

        attrs["user"] = user
        attrs["group_obj"] = group

        return attrs

    def save(self):
        user = self.validated_data["user"]
        group = self.validated_data["group_obj"]

        user.groups.clear()
        user.groups.add(group)

        return user
            
    