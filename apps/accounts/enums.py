from django.db import models

class UserTypes(models.TextChoices):
    PLAYER = ("PLAYER", "PLAYER")
    COACH = ("COACH", "COACH")
    MODERATOR = ("MODERATOR", "MODERATOR")
