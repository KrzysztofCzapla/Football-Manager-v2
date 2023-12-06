from rest_framework import viewsets, permissions
from main.models import Match
from main.serializers import MatchSerializer

class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
