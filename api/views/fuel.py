# Create your views here.
from datetime import datetime

from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from api.models import Fuel, FleetFuelRequest, FuelReceipt
from api.serializers.fuel import FuelSerializer, FleetFuelRequestSerializer, FuelReceiptSerializer, \
    FuelReceiptSummarySerializer


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

    @action(methods=['post'], detail=False, url_path='summary', url_name="summary",
            serializer_class=FuelReceiptSummarySerializer)
    def get_points(self, request):
        type = request.data['type']
        month = request.data['month']
        month = datetime.strptime(month, "%Y-%m-%d")
        total = FleetFuelRequest.objects.filter(
            type=type, created__year=month.year,
            created__month=month.month).aggregate(Sum('fuel_amount'))

        data = {'total': total['fuel_amount__sum'], 'type': type}
        return Response(data=data, status=HTTP_200_OK)


class FuelReceiptViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FuelReceipt.objects.all()
    serializer_class = FuelReceiptSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('fleet', 'user')
