from urllib.parse import urljoin

import jwt
from django.conf import settings
from django.utils import timezone
from post_office import mail
from post_office.models import PRIORITY
from rest_framework.generics import get_object_or_404
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.utils import datetime_from_epoch
from rest_framework_simplejwt.settings import api_settings

from src.apps.users.models import User
from src.apps.base.consts import EmailSubject


def send_user_verification_email(user: User) -> None:
    token = AccessToken.for_user(user)
    token.set_exp(lifetime=api_settings.REFRESH_TOKEN_LIFETIME)
    verify_email_link = urljoin(
        settings.APP_SITE,
        reverse("user-verify", (token,)),
    )
    mail.send(
        user.email,
        settings.EMAIL_HOST_USER,
        subject=str(EmailSubject.VERIFY),
        message=verify_email_link,
        priority=PRIORITY.now,
    )


def verification(token: str):
    try:
        payload = jwt.decode(
            token,
            algorithms=["HS256"],
            key=settings.SECRET_KEY,
            options={"verify_exp": False},
        )
    except jwt.InvalidSignatureError:
        return "You have sent invalid token", False

    user = get_object_or_404(User, id=payload["user_id"])
    if user.is_active:
        return "You have already verified your account", False

    claim_time = datetime_from_epoch(payload["exp"])
    if claim_time < timezone.now():
        send_user_verification_email(user)
        return (
            "The reference period has expired, "
            "we've sent a new verification link to your email",
            False,
        )

    user.is_active = True
    user.save()
    return "Successful confirmation", True


def user_change_password(serializer, user):
    if serializer.is_valid(raise_exception=True):
        user.set_password(serializer.validated_data.get("new_password"))
        user.save()
        return "Password been changed", True
    else:
        return serializer.errors, False
