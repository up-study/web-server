from rest_framework import serializers

from src.apps.base.models import Image


class ImageUploadSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Image
        fields = ("pk", "photo", "uploaded_by", "title", "size")
