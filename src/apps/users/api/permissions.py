from rest_framework import permissions


class AnotherUserToFollowUnfollowOrAccessDenied(permissions.BasePermission):

    message = "Follow / Unfollow yourself is denied"

    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.username != request.user.username
