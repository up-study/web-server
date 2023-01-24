import pytest

from rest_framework import status
from rest_framework.reverse import reverse

from src.apps.base.tests import baker


@pytest.mark.django_db
def test_get_user(api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    response = client.get(reverse("user-list"), data={})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user)
    response = client.get(reverse("user-list"), data={})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_once_user(api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    response = client.get(reverse("user-detail", (user.username,)))
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user)
    response = client.get(reverse("user-detail", (user.username,)))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_delete_user(api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    response = client.delete(reverse("user-detail", (user.username,)))
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user)
    response = client.delete(reverse("user-detail", (user.username,)))
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_update_user(api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    data = {"username": "Vasya", "email": "vasyapupkin@gmail.com"}
    response = client.put(
        reverse("user-detail", (user.username,)), data=data, format="json"
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user)
    data = {"username": "Vasya"}

    response = client.put(
        reverse("user-detail", (user.username,)), data=data, format="json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data = {"username": "Vasya", "email": "vasyapupkin@gmail.com"}
    response = client.put(
        reverse("user-detail", (user.username,)), data=data, format="json"
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_partial_update_user(api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    data = {"username": "Vasya", "email": "vasyapupkin@gmail.com"}
    response = client.patch(
        reverse("user-detail", (user.username,)), data=data, format="json"
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user)
    data = {"username": "Vasya"}
    response = client.put(
        reverse("user-detail", (user.username,)), data=data, format="json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data = {"username": "Vasya", "email": "vasyapupkin@gmail.com"}
    response = client.patch(
        reverse("user-detail", (user.username,)), data=data, format="json"
    )
    assert response.status_code == status.HTTP_200_OK
