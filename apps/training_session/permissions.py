from rest_framework.permissions import BasePermission

class TrainingSessionObjectPermission(BasePermission):

    def has_permissions(self, request, view):
        user = request.user
        if user.is_staff:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        elif user.type_of_user == 'COACH' and user.team == obj.team:
             return True
        elif user.type_of_user == 'PLAYER' and user.team == obj.team:
            allowed_actions = ['list', 'retrieve']
            return view.action in allowed_actions
        else:
            return False
