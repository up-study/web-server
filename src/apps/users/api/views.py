from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from src.apps.base.api.mixins import SerializerPerAction
from src.apps.users.api.serializers import UserSerializer, UserCreateSerializer


class UserViewSet(SerializerPerAction, ModelViewSet):
    queryset = get_user_model().objects.all()
    action_serializers = {
        "default": UserSerializer,
        "create": UserCreateSerializer,
    }
