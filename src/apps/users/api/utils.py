from post_office import mail
from post_office.models import PRIORITY

from src.upstudy.settings import EMAIL_HOST_USER


def send_email_to_user(data: dict) -> None:
    mail.send(
        data["email"],
        EMAIL_HOST_USER,
        subject=data["subject"],
        message=data["message"],
        html_message=data["html_message"],
        priority=PRIORITY.now,
    )
