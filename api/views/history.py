from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.history import FleetHistory, ToolHistory, MachineHistory
from api.serializers.history import (
    FleetHistorySerializer,
    ToolHistorySerializer,
    MachineHistorySerializer,
)


class FleetHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FleetHistory.objects.all()
    serializer_class = FleetHistorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('fleet',)


class MachineHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = MachineHistory.objects.all()
    serializer_class = MachineHistorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('machine',)


class ToolHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ToolHistory.objects.all()
    serializer_class = ToolHistorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('tool',)
