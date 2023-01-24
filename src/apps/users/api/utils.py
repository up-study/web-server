import os

from post_office import mail


def send_email_to_user(data: dict) -> None:
    email = mail.send(
        data["email"],
        os.environ.get("EMAIL_HOST_USER"),
        subject=data["subject"],
        message=data["message"],
        html_message=data["html_message"],
    )
    email.dispatch()
