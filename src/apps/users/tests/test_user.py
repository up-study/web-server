import pytest

from rest_framework import status
from rest_framework.reverse import reverse

from src.apps.base.tests import baker


@pytest.mark.django_db
def test_get_user(api_client):
    client = api_client()
    response = client.get(reverse("user-list"), data={})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_once_user(api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    response = client.get(reverse("user-detail", args=[user.username]), data={})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_user(api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    client.force_authenticate(user)
    data = {
        "username": "roma",
        "email": "user@example.com",
        "phone": "+79999999999",
        "firstName": "roma",
        "lastName": "lee",
        "type": 1,
        "githubLink": "http://example.com",
        "password": "qwerlkjvi1230v!klf",
    }
    response = client.post(reverse("user-list"), data=data, format="json")
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_delete_user(api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    client.force_authenticate(user)
    response = client.delete(reverse("user-detail", args=[user.username]), data={})
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_update_user(api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    client.force_authenticate(user)
    data = {"username": "Vasya", "email": "vasyapupkin@gmail.com"}
    response = client.put(
        reverse("user-detail", args=[user.username]), data=data, format="json"
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_partial_update_user(api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    client.force_authenticate(user)
    data = {"username": "Vasya", "email": "vasyapupkin@gmail.com"}
    response = client.patch(
        reverse("user-detail", args=[user.username]), data=data, format="json"
    )
    assert response.status_code == status.HTTP_200_OK
