from django.db import models

class PlayerPositions(models.TextChoices):
    GOALKEEPER = ("GOALKEEPER", "Goalkeeper")
    DEFENDER = ("DEFENDER", "Defender")
    MIDFIELDER = ("MIDFIELDER", "Midfielder")
    FORWARD = ("FORWARD", "Forward")

