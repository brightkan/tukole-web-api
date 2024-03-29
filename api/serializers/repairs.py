from rest_framework import serializers

from api.models import RepairHistory, Fleet, Machinery
from api.models.repairs import RepairTicket
from api.models.tools import Tool


class RepairHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairHistory
        fields = ('id', 'type', 'reason', 'cost', 'fleet', 'fleet_type', 'created', 'fm_approved')


class RepairTicketSerializer(serializers.ModelSerializer):
    object_id = serializers.SerializerMethodField(read_only=True)

    def get_object_id(self, obj):
        object_type = obj.type
        human_uuid = obj.humanUuid
        if object_type == 'fleet':
            fleet = Fleet.objects.filter(humanUuid__icontains=human_uuid).first()
            if fleet:
                return fleet.id
            return ""

        elif object_type == 'machine':
            machine = Machinery.objects.filter(humanUuid__icontains=human_uuid).first()
            if machine:
                return machine.id
            return ""
        elif object_type == 'tool':
            tool = Tool.objects.filter(humanUuid__icontains=human_uuid).first()
            if tool:
                return tool.id
            return ""

    class Meta:
        model = RepairTicket
        fields = (
            'object_id',
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
            'created',
            'humanUuid',
            'perform_fix',
            'assessment_verified',
            'assessment_verification_timestamp',
            'requisition_required',
            'repairs_started',
            'repairs_verified',
            'actual_damage',
        )
