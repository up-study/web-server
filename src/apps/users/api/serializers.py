from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from src.apps.users.models import User
from src.apps.users.api.utils import send_user_verification_email


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


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=(UniqueValidator(queryset=User.objects.all()),),
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    repeat_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "pk",
            "username",
            "email",
            "password",
            "repeat_password",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["repeat_password"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match"}
            )
        attrs.pop("repeat_password")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data, is_active=False)
        send_user_verification_email(user)

        return user


class UserChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    confirm_new_password = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = (
            "old_password",
            "new_password",
            "confirm_new_password",
        )

    def validate_old_password(self, old_password):
        user = self.context["request"].user
        if not user.check_password(old_password):
            raise serializers.ValidationError(
                {"password": "The old password is incorrect"},
            )

    def validate_new_password(self, new_password):
        old_password = self.initial_data.get("old_password")
        confirm_new_password = self.initial_data.get("confirm_new_password")
        if old_password == new_password:
            raise serializers.ValidationError(
                {"password": "Passwords match"},
            )

        if new_password != confirm_new_password:
            raise serializers.ValidationError(
                {"password": "Password do not match"},
            )

        return new_password

    def update(self, instance, validated_data):
        instance.set_password(validated_data["new_password"])
        instance.save()
        return instance


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
