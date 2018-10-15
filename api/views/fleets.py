# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.fleets import Fleet
from api.serializers.fleets import FleetSerializer


# Create your views here.

class FleetViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer
