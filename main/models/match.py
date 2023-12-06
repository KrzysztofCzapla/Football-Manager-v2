from django.db import models
from main.enums import EventStatus
from .team import Team
# Create your models here.

class Match(models.Model):
    date = models.DateField()

    time = models.TimeField()

    location = models.CharField()

    host_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="hosted_match")
    guest_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="guest_match")

    host_score = models.IntegerField(default=None, blank=True, null=True)
    guest_score = models.IntegerField(default=None, blank=True, null=True)

    match_status = models.CharField(choices=EventStatus.choices, default='SCHEDULED')