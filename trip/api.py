from .models import Mission
from rest_framework import viewsets, permissions
from .serializers import MissionSerializer


# Mission ViewSet
class MissionViewSet(viewsets.ModelViewSet):
    """
       A ViewSet for viewing and editing mission instances.
    """
    queryset = Mission.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = MissionSerializer
