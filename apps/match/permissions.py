from rest_framework.permissions import BasePermission

class MatchObjectPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff or obj.organizer == user:
            return True
        else:
            return False