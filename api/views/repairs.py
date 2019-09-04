from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import RepairHistory, Fleet
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
    filter_fields = (
        'reported_by',
        'acknowledged_by',
        'repairs_verified',
        'repairs_started',
        'requisition_required',
        'assessment_verified',
        'perform_fix',
        'repairs_complete',
    )

    def create(self, request, *args, **kwargs):
        human_uuid = request.data['humanUuid']
        if Fleet.objects.filter(humanUuid__icontains=human_uuid).exists():
            return super().create(request, *args, **kwargs)
        else:
            response = {"status": False, "message": "No fleet found with that human uuid"}
            return Response(response, status=status.HTTP_201_CREATED)
