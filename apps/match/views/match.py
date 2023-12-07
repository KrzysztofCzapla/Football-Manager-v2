from rest_framework import viewsets
from apps.match.models import Match
from apps.match.serializers import MatchSerializer

class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
