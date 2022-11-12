import pytest
from rest_framework import status
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_get_profile(api_client):
    client = api_client()
    response = client.get(reverse("user-profile"), data={})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
