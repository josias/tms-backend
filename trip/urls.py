from rest_framework import routers
from .api import MissionViewSet

router = routers.DefaultRouter()
router.register(r'api/trip/missions', MissionViewSet, basename='mission')

urlpatterns = router.urls
