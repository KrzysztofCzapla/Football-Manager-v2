from rest_framework import viewsets
from apps.match.models import Match
from apps.match.serializers import MatchSerializer

from apps.match.permissions import MatchObjectPermission

class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()

    permission_classes = [MatchObjectPermission]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)