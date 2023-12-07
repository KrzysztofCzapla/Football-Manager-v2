from django.urls import path
from .views import (
    MatchViewSet,
    MatchFilterView,
)
from rest_framework import routers

app_name = 'apps.match'

router = routers.SimpleRouter()
router.register('match', MatchViewSet)



urlpatterns = [
    path('match_schedule/', MatchFilterView.as_view(), name='match-schedule'),
] + router.urls