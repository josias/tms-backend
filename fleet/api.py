from .models import Car
from rest_framework import viewsets, permissions
from .serializers import CarSerializer


# Car ViewSet
class CarViewSet(viewsets.ModelViewSet):
    """
       A ViewSet for viewing and editing car instances.
    """
    queryset = Car.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = CarSerializer
