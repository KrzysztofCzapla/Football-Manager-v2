from rest_framework import viewsets
from apps.training_session.models import TrainingSession
from apps.training_session.serializers import TrainingSessionSerializer

class TrainingSessionViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingSessionSerializer
    queryset = TrainingSession.objects.all()