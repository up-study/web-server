from rest_framework import permissions


class NotSelfOperation(permissions.BasePermission):
    """Check if user tries to operate his own obj"""

    def has_object_permission(self, request, view, obj) -> bool:
        return request.user.pk != obj.pk
