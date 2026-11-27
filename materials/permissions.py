
from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """Проверяет, состоит ли пользователь в группе модераторов."""
    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderators").exists()


class IsOwner(BasePermission):
    """Разрешает доступ к объекту только его владельцу."""
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsModeratorOwner(BasePermission):
    """Разрешает доступ модератору или владельцу объекта."""
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        is_moderator = request.user.groups.filter(name="moderators").exists()
        return is_moderator or obj.owner == request.user


class CoursePermission(BasePermission):
    """Права доступа к курсам для модератора или владельцу."""
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        is_moderator = user.groups.filter(name="moderators").exists()

        if view.action == "create" and is_moderator:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        user = request.user

        is_moderator = user.groups.filter(name="moderators").exists()

        if is_moderator:
            return view.action in ("retrieve", "update", "partial_update",)

        return obj.owner == user


class LessonPermission(BasePermission):
    """Права доступа к урокам для модератора или владельцу."""

    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        is_moderator = user.groups.filter(name="moderators").exists()

        if request.method == "POST" and is_moderator:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        user = request.user

        is_moderator = user.groups.filter(name="moderators").exists()

        if is_moderator:
            return request.method in ("GET", "PUT", "PATCH")

        return obj.course.owner == user
