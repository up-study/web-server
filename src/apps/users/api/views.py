from src.apps.users.models import User
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
    FollowUserSerializer,
    UserListSerializer,
)


class UserViewSet(SerializerPerAction, ModelViewSet):
    queryset = User.objects.all()
    action_serializers = {
        "default": UserSerializer,
        "create": UserCreateSerializer,
        "profile": ProfileUserSerializer,
        "follow": FollowUserSerializer,
        "followers": UserListSerializer,
        "following": UserListSerializer,
    }
    lookup_field = "username"

    @action(detail=False, methods=["GET"], permission_classes=[IsAuthenticated])
    def profile(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["GET"], permission_classes=[IsAuthenticated])
    def followers(self, *args, **kwargs):
        user = self.get_object()
        queryset = user.followers.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], permission_classes=[IsAuthenticated])
    def following(self, *args, **kwargs):
        user = self.get_object()
        queryset = user.following.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["POST"], permission_classes=[IsAuthenticated])
    def follow(self, request: Request, *args, **kwargs):
        user = self.get_object()
        request.user.following.add(user)
        return Response("Successfully")
