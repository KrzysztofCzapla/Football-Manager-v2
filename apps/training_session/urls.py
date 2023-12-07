from django.urls import path
from .views import TrainingSessionViewSet, TrainingSessionFilterView
from rest_framework import routers

app_name = 'apps.training_session'

router = routers.SimpleRouter()
router.register('training_session', TrainingSessionViewSet)



urlpatterns = [
    path('training_session_schedule/', TrainingSessionFilterView.as_view(), name='training-session-schedule'),
] + router.urls