from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import Cost
from api.serializers.cost import CostSerializer


class CostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site',)
