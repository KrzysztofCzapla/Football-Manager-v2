from rest_framework import viewsets
from main.models import Player
from main.serializers import PlayerSerializer
from rest_framework.parsers import MultiPartParser

class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    parser_classes = [MultiPartParser]
