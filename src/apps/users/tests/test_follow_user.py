import pytest

from rest_framework import status
from rest_framework.reverse import reverse

from src.apps.base.tests import baker


@pytest.mark.django_db
def test_follow_user(api_client):
    following_user = baker.make_recipe("users.user")
    user = baker.make_recipe("users.user")
    client = api_client()
    client.force_authenticate(following_user)
    response = client.post(reverse("user-follow", args=[user.username]), data={})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_unfollow_user(api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    client.force_authenticate(user)
    response = client.post(reverse("user-unfollow", args=[user.username]), data={})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_list_followers(api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    client.force_authenticate(user)
    response = client.get(reverse("user-followers", args=[user.username]), data={})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_list_following(api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    client.force_authenticate(user)
    response = client.get(reverse("user-following", args=[user.username]), data={})
    assert response.status_code == status.HTTP_200_OK
