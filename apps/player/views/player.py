from rest_framework import viewsets
from apps.player.models import Player
from apps.player.serializers import PlayerSerializer
from rest_framework.parsers import MultiPartParser
from apps.player.permissions import PlayerObjectPermission
from django.contrib.auth import get_user_model

User = get_user_model()

class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    parser_classes = [MultiPartParser]

    permission_classes = [PlayerObjectPermission]