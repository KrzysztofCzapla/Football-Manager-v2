from django.db import models
from apps.common.models import Country
# Create your models here.

class Team(models.Model):
    name = models.CharField()

    description = models.TextField(null=True, blank=True)

    logo = models.ImageField(upload_to='teams_logos/', null=True, blank=True)

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, default=None, null=True, blank=True)
