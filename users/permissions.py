from rest_framework.permissions import BasePermission


class IsUserOwner(BasePermission):
    """Разрешает пользователю работать только со своим профилем."""
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj == request.user
