from rest_framework import serializers
from main.models import TrainingSession

class TrainingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSession
        fields = '__all__'