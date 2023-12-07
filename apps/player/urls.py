from .views import PlayerViewSet
from rest_framework import routers

app_name = 'apps.player'

router = routers.SimpleRouter()
router.register('player', PlayerViewSet)



urlpatterns = [
] + router.urls