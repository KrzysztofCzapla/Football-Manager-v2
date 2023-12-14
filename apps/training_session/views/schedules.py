from rest_framework import generics
from apps.training_session.models import TrainingSession
from apps.training_session.serializers import TrainingSessionSerializer
from apps.training_session.filters import TrainingSessionFilter
from django_filters import rest_framework as filters

class TrainingSessionFilterView(generics.ListAPIView):
    queryset = TrainingSession.objects.all()
    serializer_class = TrainingSessionSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TrainingSessionFilter