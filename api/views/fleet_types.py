# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.fleet_types import FleetType
from api.serializers.fleet_types import FleetTypeSerializer


# Create your views here.

class Fleet_typesViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FleetType.objects.all()
    serializer_class = FleetTypeSerializer
