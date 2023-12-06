from django.urls import path
from .views import (
    PlayerViewSet,
    TrainingSessionViewSet,
    MatchViewSet,
    TeamViewSet,
    MatchFilterView,
    TrainingSessionFilterView
)
from rest_framework import routers

app_name = 'main'

router = routers.SimpleRouter()
router.register('player', PlayerViewSet)
router.register('match', MatchViewSet)
router.register('team', TeamViewSet)
router.register('training_session', TrainingSessionViewSet)


urlpatterns = [
    path('match_schedule/', MatchFilterView.as_view(), name='match-schedule'),
    path('training_schedule/', TrainingSessionFilterView.as_view(), name='training-schedule'),
] + router.urls