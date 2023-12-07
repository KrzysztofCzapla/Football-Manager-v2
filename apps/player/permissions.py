from rest_framework.permissions import BasePermission

class PlayerObjectPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        elif user.type_of_user == 'COACH':
            allowed_actions = ['list', 'retrieve']
            return view.action in allowed_actions
        elif user.type_of_user == 'PLAYER':
            if obj.user == request.user:
                return True
            allowed_actions = ['list', 'retrieve']
            return view.action in allowed_actions
        else:
            return False
