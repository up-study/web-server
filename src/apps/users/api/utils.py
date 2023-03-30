import jwt
from urllib.parse import urljoin

from django.conf import settings
from post_office import mail
from post_office.models import PRIORITY
from rest_framework.generics import get_object_or_404
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import AccessToken

from src.apps.users.models import User
from src.apps.base.consts import EmailSubject


def send_user_verification_email(user: User) -> None:
    token = str(AccessToken.for_user(user))
    verify_email_link = urljoin(
        settings.APP_SITE,
        reverse("user-verify", (token,)),
    )
    data = {
        "email": user.email,
        "subject": str(EmailSubject.VERIFY),
        "message": verify_email_link,
    }
    mail.send(
        data["email"],
        settings.EMAIL_HOST_USER,
        subject=data["subject"],
        message=data["message"],
        priority=PRIORITY.now,
    )


def verification(token: str):
    try:
        payload = jwt.decode(
            token,
            algorithms=["HS256"],
            key=settings.SECRET_KEY,
        )
        user = get_object_or_404(User, id=payload["user_id"])

    except jwt.ExpiredSignatureError:
        return "The reference period has expired", False

    except jwt.InvalidSignatureError:
        return "You have sent invalid token", False

    if user.is_active:
        return "You have already verified your account", False

    user.is_active = True
    user.save()
    return "Successful confirmation", True
