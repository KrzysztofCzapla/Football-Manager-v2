from django.db import models
from apps.team.models.team import Team
from apps.player.models.player import Player
from apps.training_session.enums import EventStatus


class TrainingSession(models.Model):
    date = models.DateField()

    time = models.TimeField()

    location = models.CharField()

    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    attendees = models.ManyToManyField(Player, blank=True)

    training_status = models.CharField(choices=EventStatus.choices, default='SCHEDULED')