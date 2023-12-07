import django_filters
from .models import Match

class MatchFilter(django_filters.FilterSet):

    class Meta:
        model = Match
        fields = ['date', 'time', 'location', 'host_team', 'guest_team','match_status']