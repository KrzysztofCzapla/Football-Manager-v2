from rest_framework import serializers
from apps.match.models import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ("date", "time", "location", "host_team", "guest_team", "host_score", "guest_score", "match_status")