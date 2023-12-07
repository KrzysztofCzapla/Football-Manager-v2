from rest_framework import viewsets
from apps.main.models import Match
from apps.main.serializers import MatchSerializer

class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
