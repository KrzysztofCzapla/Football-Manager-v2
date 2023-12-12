from django.db import models
from apps.player.enums import PlayerPositions
from apps.team.models import Team
from apps.accounts.models import CustomUser
from apps.common.models import Country

class Player(models.Model):
    name = models.CharField()

    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    position = models.CharField(choices=PlayerPositions.choices)

    date_of_birth = models.DateField()

    country_of_origin = models.ForeignKey(Country, on_delete=models.SET_NULL, default=None, null=True, blank=True)

    phone_number = models.CharField(max_length=12)

    photo = models.ImageField(upload_to='player_photos/', null=True, blank=True)

    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, default=None, null=True, blank=True)
