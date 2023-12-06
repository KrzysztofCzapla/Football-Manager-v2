from django.db import models
from main.enums import PlayerPositions
from .team import Team
# Create your models here.

class Player(models.Model):
    name = models.CharField()

    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    position = models.CharField(choices=PlayerPositions.choices)

    date_of_birth = models.DateField()

    nationality = models.CharField()

    phone_number = models.CharField(max_length=12)

    photo = models.ImageField(upload_to='player_photos/', null=True, blank=True)
