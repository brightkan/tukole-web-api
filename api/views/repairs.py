from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import RepairHistory
from api.models.repairs import RepairTicket
from api.serializers.repairs import RepairHistorySerializer, RepairTicketSerializer


class RepairHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = RepairHistory.objects.all()
    serializer_class = RepairHistorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('fleet', 'fleet_type')


class RepairTicketViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = RepairTicket.objects.all()
    serializer_class = RepairTicketSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('fleet', 'fleet_type')
