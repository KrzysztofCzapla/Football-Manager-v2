from rest_framework import serializers
from apps.player.models import Player
from apps.common.serializers import CountrySerializer

class PlayerSerializer(serializers.ModelSerializer):
    country_of_origin = CountrySerializer(read_only=True)
    class Meta:
        model = Player
        fields = ('name', 'team', 'position', 'date_of_birth', 'country_of_origin', 'phone_number', 'photo')