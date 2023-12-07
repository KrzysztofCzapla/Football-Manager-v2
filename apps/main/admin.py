from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Match)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(TrainingSession)