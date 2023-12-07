from rest_framework import serializers
from apps.training_session.models import TrainingSession

class TrainingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSession
        fields = ('date', 'time', 'location', 'team', 'attendees', 'training_status')