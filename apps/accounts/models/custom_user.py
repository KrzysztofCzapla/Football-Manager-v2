from apps.accounts.enums import UserTypes
from apps.main.models.team import Team
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    type_of_user = models.CharField(choices=UserTypes.choices, default=None, blank=True, null=True)

    team = models.ForeignKey(Team, on_delete=models.SET_NULL, default=None, null=True, blank=True)