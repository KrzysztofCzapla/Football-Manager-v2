from rest_framework import serializers
from apps.team.models import Team
from apps.common.serializers import CountrySerializer

class TeamSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    class Meta:
        model = Team
        fields = ('name', 'description', 'logo', 'country', 'owner', 'coach')