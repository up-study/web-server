import os
from uuid import uuid4

from django.db import models


class Image(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    photo = models.ImageField(upload_to="images")
    uploaded_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="uploaded_images"
    )

    def __str__(self):
        return f"{self.uuid} | {self.photo.name} "

    @property
    def title(self) -> str:
        return os.path.split(self.photo.file.name)[-1]

    @property
    def size(self) -> str:
        return self.photo.file.size
