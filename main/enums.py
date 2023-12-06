from django.db import models

class PlayerPositions(models.TextChoices):
    GK = ("GK", "Goalkeeper")
    DEF = ("DEF", "Defender")
    MID = ("MID", "Midfielder")
    FOR = ("FOR", "Forward")

class EventStatus(models.TextChoices):
    SCHEDULED = ("SCHEDULED", "Scheduled")
    STARTED = ("STARTED", "Started")
    ENDED = ("ENDED", "Ended")

