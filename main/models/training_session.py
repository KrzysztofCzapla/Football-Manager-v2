from django.db import models
from .team import Team
from .player   import Player
from main.enums import EventStatus


class TrainingSession(models.Model):
    date = models.DateField()

    time = models.TimeField()

    location = models.CharField()

    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    attendees = models.ManyToManyField(Player, blank=True)

    training_status = models.CharField(choices=EventStatus.choices, default='SCHEDULED')