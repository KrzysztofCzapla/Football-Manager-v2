from django.db import models
# Create your models here.

class Team(models.Model):
    name = models.CharField()

    description = models.TextField(null=True, blank=True)

    logo = models.ImageField(upload_to='teams_logos/', null=True, blank=True)
