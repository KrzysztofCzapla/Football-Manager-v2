from rest_framework import generics
from apps.match.models import Match
from apps.match.serializers import MatchSerializer
from apps.match.filters import MatchFilter
from django_filters import rest_framework as filters

class MatchFilterView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MatchFilter
