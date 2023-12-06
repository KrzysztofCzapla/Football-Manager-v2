from rest_framework import viewsets
from main.models import TrainingSession
from main.serializers import TrainingSessionSerializer

class TrainingSessionViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingSessionSerializer
    queryset = TrainingSession.objects.all()