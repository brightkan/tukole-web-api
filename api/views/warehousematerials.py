# Create your views here.

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.warehousematerials import WarehouseMaterial
from api.serializers.warehousematerials import WarehouseMaterialSerializer


# Create your views here.


class WarehouseMaterialViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = WarehouseMaterial.objects.all()
    serializer_class = WarehouseMaterialSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site', 'material')
