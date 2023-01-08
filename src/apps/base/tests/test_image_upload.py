import io

from PIL import Image as PILImage
import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from src.apps.base.tests import baker
from src.apps.base.models import Image


@pytest.fixture
def upload_photo():
    file = io.BytesIO()
    image = PILImage.new("RGBA", size=(100, 100), color=(155, 0, 0))
    image.save(file, "png")
    file.name = "test.png"
    file.seek(0)
    return {"photo": file}


@pytest.mark.django_db
def test_image_upload(upload_photo, api_client):
    user = baker.make_recipe("users.user")
    client = api_client()
    client.force_authenticate(user)
    response = client.post(reverse("images-upload"), upload_photo, format="multipart")
    assert response.status_code == status.HTTP_201_CREATED, response.data
    assert (
        uploaded_by := Image.objects.get(pk=response.data.get("pk")).uploaded_by
    ) == user, uploaded_by
