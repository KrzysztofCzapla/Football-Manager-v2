from django.db import models

class EventStatus(models.TextChoices):
    SCHEDULED = ("SCHEDULED", "Scheduled")
    STARTED = ("STARTED", "Started")
    ENDED = ("ENDED", "Ended")

