from django.contrib.auth import get_user_model
from rest_framework import serializers

from src.apps.users.consts import RoleCreateSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name"
        )


class UserCreateSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=RoleCreateSerializer)

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "role",
            "github_link",
            "password"
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data: dict):
        return self.Meta.model.objects.create_user(**validated_data)


class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "role",
            "github_link"
        )
