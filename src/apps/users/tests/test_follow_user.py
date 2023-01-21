import pytest

from rest_framework import status
from rest_framework.reverse import reverse

from src.apps.base.tests import baker


@pytest.mark.django_db
def test_follow_user(api_client):
    user = baker.make_recipe("users.user")
    user_to_follow = baker.make_recipe("users.user")

    client = api_client()
    response = client.put(reverse("user-follow", (user_to_follow.username,)))
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user)
    response = client.put(reverse("user-follow", (user_to_follow.username,)))
    assert response.status_code == status.HTTP_200_OK, response.data

    # cannot follow twice
    response = client.put(reverse("user-follow", (user_to_follow.username,)))
    assert response.status_code == status.HTTP_226_IM_USED, response.data

    # user cannot follow himself
    response = client.put(reverse("user-follow", (user.username,)))
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.data

    response = client.put(reverse("user-follow", ("user",)))
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_unfollow_user(api_client):
    user = baker.make_recipe("users.user")
    user_to_unfollow = baker.make_recipe("users.user")
    client = api_client()
    response = client.put(reverse("user-unfollow", (user_to_unfollow.username,)))
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user)

    # must fail with 226 since he is not following any user
    response = client.put(reverse("user-unfollow", (user_to_unfollow.username,)))
    assert response.status_code == status.HTTP_226_IM_USED

    # start follow to later unfollow test
    user.following.add(user_to_unfollow)

    # should unfollow successfully
    response = client.put(reverse("user-unfollow", (user_to_unfollow.username,)))
    assert response.status_code == status.HTTP_200_OK, response.data
    assert not user.following.contains(user_to_unfollow)

    # cannot unfollow twice
    response = client.put(reverse("user-unfollow", (user_to_unfollow.username,)))
    assert response.status_code == status.HTTP_226_IM_USED, response.data

    # user cannot unfollow himself
    response = client.put(reverse("user-unfollow", (user.username,)))
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.data

    response = client.put(reverse("user-unfollow", ("user",)))
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_get_list_followers(api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    response = client.get(reverse("user-followers", (user.username,)))
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user)
    response = client.get(reverse("user-followers", (user.username,)))
    assert response.status_code == status.HTTP_200_OK

    response = client.get(reverse("user-followers", ("user",)))
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_get_list_following(api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    response = client.get(reverse("user-following", (user.username,)))
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user)
    response = client.get(reverse("user-following", (user.username,)))
    assert response.status_code == status.HTTP_200_OK

    response = client.get(reverse("user-following", ("user",)))
    assert response.status_code == status.HTTP_404_NOT_FOUND
