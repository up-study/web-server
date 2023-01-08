from django.urls import path

from src.apps.base.api.views import UploadImageAPIView


urlpatterns = [
    path("images/upload/", UploadImageAPIView.as_view(), name="images-upload"),
]
