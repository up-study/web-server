from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from src.apps.users.models import User
from src.apps.base.api.mixins import PermissionPerAction, SerializerPerAction
from src.apps.users.api.serializers import (
    UserSerializer,
    UserCreateSerializer,
    ProfileUserSerializer,
    UserListSerializer,
)
from src.apps.users.api.permissions import NotSelfOperation


class UserViewSet(SerializerPerAction, PermissionPerAction, ModelViewSet):
    queryset = User.objects.all()
    action_serializers = {
        "default": UserSerializer,
        "create": UserCreateSerializer,
        "profile": ProfileUserSerializer,
        "follow": None,
        "unfollow": None,
        "followers": UserListSerializer,
        "following": UserListSerializer,
    }
    action_permissions = {
        "default": (IsAuthenticated,),
    }
    lookup_field = "username"

    @action(detail=False, methods=["GET"], permission_classes=[IsAuthenticated])
    def profile(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

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

    @action(
        detail=True,
        methods=["PUT", "PATCH"],
        permission_classes=[IsAuthenticated, NotSelfOperation],
    )
    def follow(self, request: Request, *args, **kwargs):
        user = self.get_object()
        if request.user.following.contains(user):
            return Response(
                "You are already following this user", status.HTTP_226_IM_USED
            )
        request.user.following.add(user)
        return Response("Successfully")

    @action(
        detail=True,
        methods=["PUT", "PATCH"],
        permission_classes=[IsAuthenticated, NotSelfOperation],
    )
    def unfollow(self, request: Request, *args, **kwargs):
        user = self.get_object()
        if not request.user.following.contains(user):
            return Response("You are not following this user", status.HTTP_226_IM_USED)
        request.user.following.remove(user)
        return Response("Successfully")
