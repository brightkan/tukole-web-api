from rest_framework import serializers

from api.models import RepairHistory
from api.models.repairs import RepairTicket


class RepairHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairHistory
        fields = ('id', 'type', 'reason', 'cost', 'fleet', 'fleet_type', 'created', 'fm_approved')


class RepairTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairTicket
        fields = (
            'reported_by',
            'time_reported',
            'time_acknowledged',
            'acknowledged_by',
            'assessment',
            'requisition_materials',
            'requisition_started',
            'requisition_ended',
            'repairs_complete',
            'repairs_complete_timestamp',
            'mechanic',
            'type',
            'supervised_by',
            'id',
            'created'
            'humanUuid',
            'perform_fix',
            'assessment_verified',
            'assessment_verification_timestamp',
            'requisition_required',
            'repairs_started',
            'repairs_verified',

        )
