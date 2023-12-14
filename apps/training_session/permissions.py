from rest_framework.permissions import BasePermission, SAFE_METHODS
from apps.team.models import Team

class TrainingSessionObjectPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        team = Team.objects.get(pk=request.data['team'])
        if user == team.coach or user == team.owner or user.is_staff:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff or obj.team.coach == user:
            return True
        else:
            return False