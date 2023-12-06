import django_filters
from .models import Match, TrainingSession

class MatchFilter(django_filters.FilterSet):

    class Meta:
        model = Match
        fields = ['date', 'time', 'location', 'host_team', 'guest_team','match_status']

class TrainingSessionFilter(django_filters.FilterSet):

    class Meta:
        model = TrainingSession
        fields = ['date', 'time', 'location', 'team', 'attendees', 'training_status']