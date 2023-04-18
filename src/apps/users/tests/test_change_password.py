import pytest

from rest_framework.reverse import reverse
from rest_framework import status

from src.apps.base.tests import baker


@pytest.mark.django_db
@pytest.mark.parametrize(
    "old_password, new_password, confirm_new_password, status_code",
    [
        ("password123", "new_password", "new_password", status.HTTP_200_OK),
        ("wrong_password", "new_password", "new_password", status.HTTP_400_BAD_REQUEST),
        ("password123", "new_password", "wrong_password", status.HTTP_400_BAD_REQUEST),
        ("password123", "password123", "password123", status.HTTP_400_BAD_REQUEST),
    ]
)
def test_password_change(api_client, old_password, new_password, confirm_new_password, status_code):
    client = api_client()
    user = baker.make_recipe("users.user")
    user.set_password("password123")
    client.force_authenticate(user)

    response = client.patch(
        reverse("user-change-password", kwargs={"username": user.username}),
        data={
            "old_password": old_password,
            "new_password": new_password,
            "confirm_new_password": confirm_new_password,
        },
        format="json"
    )

    assert response.status_code == status_code
