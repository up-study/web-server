import pytest

from django.core import mail
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from src.apps.base.tests import baker
from src.apps.users.models import User
from src.upstudy.settings import SITE


@pytest.mark.django_db
def test_register_user(api_client, mailoutbox, freezer):
    client = api_client()
    user = baker.make_recipe("users.user")
    client.force_authenticate(user)
    data = {
        "username": "usertest",
        "email": "test@example.com",
        "password": "aldfglse123",
        "repeat_password": "aldfglse123",
    }

    # register user
    response = client.post(reverse("user-list"), data=data, format="json")
    assert response.status_code == status.HTTP_201_CREATED

    # send mail with token
    new_user = User.objects.get(username=data["username"])
    assert not new_user.is_active

    token = str(RefreshToken.for_user(new_user).access_token)
    assert token

    mailoutbox.clear()
    mail.send_mail(
        "subjects",
        f"{SITE}{reverse('user-verify', (token,))}",
        "server@example.com",
        [new_user.email],
    )
    mail_from_server = mailoutbox[0]

    # send just one email
    assert len(mailoutbox) == 1, mailoutbox

    # the body equal
    assert mail_from_server.body == f"{SITE}{reverse('user-verify', (token,))}"

    # checking the confirmation link
    response = client.get(reverse("user-verify", (token,)))
    assert response.status_code == status.HTTP_200_OK

    # checking user verify
    new_user = User.objects.get(username=data["username"])
    assert new_user.is_active

    # invalid token
    response = client.get(reverse("user-verify", (token + "invalid",)))
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # period has expired
    freezer.move_to("2023-5-20")
    response = client.get(reverse("user-verify", (token,)))
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # user with that username already exists
    response = client.post(reverse("user-list"), data=data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
