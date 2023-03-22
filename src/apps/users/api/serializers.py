from dotenv import load_dotenv

from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken

from src.apps.users.models import User
from src.apps.users.api.utils import send_email_to_user
from src.upstudy.settings import SITE
from src.upstudy.settings import EmailSubject

load_dotenv()


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

        user.set_password(validated_data["password"])
        user.save()

        token = str(RefreshToken.for_user(user).access_token)
        verify_email_link = f"{SITE}{reverse('user-verify', (token,))}"
        data = {
            "email": validated_data["email"],
            "subject": str(EmailSubject.VERIFY),
            "message": "Confirm your email",
            "html_message": verify_email_link,
        }
        send_email_to_user(data)

        return user


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
