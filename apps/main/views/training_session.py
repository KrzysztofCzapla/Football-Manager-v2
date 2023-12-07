from rest_framework import viewsets
from apps.main.models import TrainingSession
from apps.main.serializers import TrainingSessionSerializer

class TrainingSessionViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingSessionSerializer
    queryset = TrainingSession.objects.all()