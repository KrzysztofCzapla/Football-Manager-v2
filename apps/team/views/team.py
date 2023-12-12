from rest_framework import viewsets
from apps.team.models import Team
from apps.team.serializers import TeamSerializer
from rest_framework.parsers import MultiPartParser
from apps.team.permissions import TeamObjectPermission

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    parser_classes = [MultiPartParser]

    permission_classes = [TeamObjectPermission]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)