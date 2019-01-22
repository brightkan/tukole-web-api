# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import Fuel
from api.serializers.fuel import FuelSerializer


class FuelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('fleet', 'fueled_by')
