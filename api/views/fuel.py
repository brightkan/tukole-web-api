# Create your views here.
from datetime import datetime

import django_filters
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from api.models import Fuel, FleetFuelRequest, FuelReceipt
from api.serializers.fuel import (
    FuelSerializer,
    FleetFuelRequestSerializer,
    FuelReceiptSerializer,
    FuelReceiptSummarySerializer,
)


class FuelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('fleet', 'fueled_by')


# class FleetFuelRequestFilter(FilterSet):
#     start_date_gte = django_filters.DateTimeFilter(name="created", lookup_expr='gte')
#     end_date_lte = django_filters.DateTimeFilter(name="created", lookup_expr='ltr')
#
#     class Meta:
#         model = FleetFuelRequest
#         fields = ['fleet', 'user', 'start_date_gte', 'end_date_lte']


class FleetFuelRequestFilter(django_filters.FilterSet):
    "Custom meeting filtering by start date"

    class Meta:
        model = FleetFuelRequest
        fields = {'user': ['exact'], 'type': ['exact'], 'created': ['gte', 'lt']}


class FleetFuelRequestViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FleetFuelRequest.objects.all()
    serializer_class = FleetFuelRequestSerializer
    filter_class = FleetFuelRequestFilter
    filter_backends = (DjangoFilterBackend,)

    @action(
        methods=['post'],
        detail=False,
        url_path='summary',
        url_name="summary",
        serializer_class=FuelReceiptSummarySerializer,
    )
    def get_points(self, request):
        type = request.data['type']
        month = request.data['month']
        month = datetime.strptime(month, "%Y-%m-%d")
        total = FleetFuelRequest.objects.filter(
            type=type, created__year=month.year, created__month=month.month
        ).aggregate(Sum('approved_amount'))

        data = {'total': total['approved_amount__sum'], 'type': type}
        return Response(data=data, status=HTTP_200_OK)


class FuelReceiptViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FuelReceipt.objects.all()
    serializer_class = FuelReceiptSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('fleet', 'user')
