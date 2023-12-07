from .views import TeamViewSet
from rest_framework import routers

app_name = 'apps.team'

router = routers.SimpleRouter()
router.register('team', TeamViewSet)

urlpatterns = [
] + router.urls