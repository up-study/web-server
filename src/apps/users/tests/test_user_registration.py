import pytest
from urlextract import URLExtract

from rest_framework.reverse import reverse
from rest_framework import status

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

    # send mail with token
    new_user = User.objects.get(username=user_create_data["username"])
    assert not new_user.is_active

    mail_from_server = mailoutbox[0]

    # send just one email
    assert len(mailoutbox) == 1, mail_from_server

    url_from_message = URLExtract().find_urls(mail_from_server.body)[0]

    # checking the confirmation link
    response = client.get(url_from_message)
    assert response.status_code == status.HTTP_200_OK

    # checking user verify
    new_user = User.objects.get(username=user_create_data["username"])
    assert new_user.is_active

    # invalid token
    response = client.get(url_from_message)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # period has expired
    freezer.move_to("2023-5-20")
    response = client.get(url_from_message)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # user with that username already exists
    response = client.post(reverse("user-list"), data=user_create_data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
