from django.db import models


class Image(models.Model):
    photo = models.ImageField(verbose_name="Image")

    class Meta:
        verbose_name_plural = "Image"
