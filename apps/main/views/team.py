from rest_framework import viewsets
from apps.main.models import Team
from apps.main.serializers import TeamSerializer
from rest_framework.parsers import MultiPartParser

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    parser_classes = [MultiPartParser]