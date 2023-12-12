from django.db import models
from apps.match.enums import EventStatus
from apps.team.models import Team
from apps.accounts.models import CustomUser

class Match(models.Model):
    organizer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, default=None, null=True, blank=True, related_name="organized_match")

    date = models.DateField()

    time = models.TimeField()

    location = models.CharField()

    host_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="hosted_match")
    guest_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="guest_match")

    host_score = models.IntegerField(default=None, blank=True, null=True)
    guest_score = models.IntegerField(default=None, blank=True, null=True)

    match_status = models.CharField(choices=EventStatus.choices, default='SCHEDULED')