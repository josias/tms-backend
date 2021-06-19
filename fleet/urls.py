from rest_framework import routers
from .api import CarViewSet

router = routers.DefaultRouter()
router.register(r'api/fleet/cars', CarViewSet, basename='car')

urlpatterns = router.urls
