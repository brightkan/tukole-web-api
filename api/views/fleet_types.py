# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.fleet_types import Fleet_types
from api.serializers.fleet_types import Fleet_typesSerializer


# Create your views here.

class Fleet_typesViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Fleet_types.objects.all()
    serializer_class = Fleet_typesSerializer
