from rest_framework.permissions import BasePermission

class TeamObjectPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.is_staff:
            return True
        elif user.type_of_user == 'COACH' or user.type_of_user == 'PLAYER':
            allowed_actions = ['list', 'retrieve']
            return view.action in allowed_actions
        else:
            return False
