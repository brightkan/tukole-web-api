# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import Fuel, FleetFuelRequest, FuelReceipt
from api.serializers.fuel import FuelSerializer, FleetFuelRequestSerializer, FuelReceiptSerializer


class FuelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('fleet', 'fueled_by')


class FleetFuelRequestViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FleetFuelRequest.objects.all()
    serializer_class = FleetFuelRequestSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('fleet', 'user')


class FuelReceiptViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FuelReceipt.objects.all()
    serializer_class = FuelReceiptSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('fleet', 'user')
