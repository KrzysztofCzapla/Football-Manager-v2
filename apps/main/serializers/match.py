from rest_framework import serializers
from apps.main.models import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'