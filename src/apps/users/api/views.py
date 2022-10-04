from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from src.apps.base.api.mixins import SerializerPerAction
from src.apps.users.api.serializers import (
    UserSerializer,
    UserCreateSerializer,
    ProfileUserSerializer,
)


class UserViewSet(SerializerPerAction, ModelViewSet):
    queryset = get_user_model().objects.all()
    action_serializers = {
        "default": UserSerializer,
        "create": UserCreateSerializer,
        "profile": ProfileUserSerializer,
    }

    @action(detail=False, methods=["GET"], permission_classes=[IsAuthenticated])
    def profile(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
