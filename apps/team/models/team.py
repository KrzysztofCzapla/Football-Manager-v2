from django.db import models
from apps.common.models import Country
from apps.accounts.models import CustomUser

class Team(models.Model):
    name = models.CharField()

    description = models.TextField(null=True, blank=True)

    logo = models.ImageField(upload_to='teams_logos/', null=True, blank=True)

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, default=None, null=True, blank=True)

    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, default=None, null=True, blank=True, related_name="owned_team")

    coach = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, default=None, null=True, blank=True, related_name="coached_team")
