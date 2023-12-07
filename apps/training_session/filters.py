import django_filters
from .models import TrainingSession

class TrainingSessionFilter(django_filters.FilterSet):

    class Meta:
        model = TrainingSession
        fields = ['date', 'time', 'location', 'team', 'attendees', 'training_status']