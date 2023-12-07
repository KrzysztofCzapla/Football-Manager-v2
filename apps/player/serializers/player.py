from rest_framework import serializers
from apps.player.models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'team', 'position', 'date_of_birth', 'nationality', 'phone_number', 'photo')