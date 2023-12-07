from rest_framework import generics
from apps.main.models import Match, TrainingSession
from apps.main.serializers import MatchSerializer, TrainingSessionSerializer
from apps.main.filters import MatchFilter, TrainingSessionFilter
from django_filters import rest_framework as filters

class MatchFilterView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MatchFilter

class TrainingSessionFilterView(generics.ListAPIView):
    queryset = TrainingSession.objects.all()
    serializer_class = TrainingSessionSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TrainingSessionFilter