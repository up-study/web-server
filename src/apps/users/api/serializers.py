from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from src.apps.users.models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "phone",
            "first_name",
            "last_name",
            "type",
            "followers_amount",
            "following_amount",
        )


class UserCreateSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField()

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "phone",
            "first_name",
            "last_name",
            "type",
            "github_link",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data: dict):
        return self.Meta.model.objects.create_user(**validated_data)


class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "phone",
            "first_name",
            "last_name",
            "type",
            "github_link",
        )
