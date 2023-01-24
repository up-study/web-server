import pytest

from rest_framework.reverse import reverse
from rest_framework import status


@pytest.mark.django_db
def test_register_user(api_client):
    client = api_client()
    data = {
        "username": "usertest",
        "email": "test@example.com",
        "password": "aldfglse123",
        "repeat_password": "aldfglse123",
    }

    # register user
    response = client.post(reverse("user-list"), data=data, format="json")
    assert response.status_code == status.HTTP_201_CREATED

    # user with that username already exists
    response = client.post(reverse("user-list"), data=data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
