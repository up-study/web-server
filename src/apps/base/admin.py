from django.contrib import admin

from src.apps.base.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
