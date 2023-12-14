from rest_framework.permissions import BasePermission

class PlayerObjectPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff or user == obj.user:
            return True
        else:
            return False
