from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from src.apps.base.api.serializers import ImageUploadSerializer


class UploadImageAPIView(CreateAPIView):
    serializer_class = ImageUploadSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
