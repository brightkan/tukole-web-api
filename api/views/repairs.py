from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import RepairHistory, Fleet, Machinery
from api.models.repairs import RepairTicket
from api.models.tools import Tool
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

        if request.data['type'] == 'fleet':
            if Fleet.objects.filter(humanUuid__icontains=human_uuid).exists():
                return super().create(request, *args, **kwargs)
        elif request.data['type'] == 'machine':
            if Machinery.objects.filter(humanUuid__icontains=human_uuid).exists():
                return super().create(request, *args, **kwargs)
        elif request.data['type'] == 'tool':
            if Tool.objects.filter(humanUuid__icontains=human_uuid).exists():
                return super().create(request, *args, **kwargs)
        else:
            response = {"status": False, "message": "No %s found with that human uuid" % request.data['object_type']}
            return Response(response, status=status.HTTP_201_CREATED)
