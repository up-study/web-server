import pytest
from urlextract import URLExtract

from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework_simplejwt.settings import api_settings

from src.apps.users.models import User


@pytest.fixture
def user_create_data():
    return {
        "username": "usertest",
        "email": "test@example.com",
        "password": "aldfglse123",
        "repeat_password": "aldfglse123",
    }


@pytest.mark.django_db
def test_register_user(api_client, user_create_data, mailoutbox, freezer):
    client = api_client()

    # register user
    response = client.post(reverse("user-list"), data=user_create_data, format="json")
    assert response.status_code == status.HTTP_201_CREATED

    # user should be inactive
    user = User.objects.get(pk=response.data["pk"])
    assert not user.is_active

    # send just one email
    assert len(mailoutbox) == 1, mailoutbox

    # TODO: check invalid token
    # TODO: check user not found

    # period has expired
    mail_from_server = mailoutbox[-1]
    url_from_message = URLExtract().find_urls(mail_from_server.body)[0]
    freezer.move_to(api_settings.REFRESH_TOKEN_LIFETIME)
    response = client.get(url_from_message)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.data
    assert len(mailoutbox) == 2, mailoutbox

    # verifying user
    mail_from_server = mailoutbox[-1]
    url_from_message = URLExtract().find_urls(mail_from_server.body)[0]
    response = client.get(url_from_message)
    assert response.status_code == status.HTTP_200_OK

    # checking user verify
    user.refresh_from_db()
    assert user.is_active

    # 400 error: user already has been verified
    response = client.get(url_from_message)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # user with that username already exists
    response = client.post(reverse("user-list"), data=user_create_data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
