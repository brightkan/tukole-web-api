from rest_framework import serializers

from api.models import Machinery
from api.models.fleets import Fleet, UserFleetAssignment
from api.serializers.machinery import MachinerySerializer


class FleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fleet
        fields = ('id', 'name', 'vehicle_type', 'uuid', 'humanUuid', 'status', 'workspace', 'created')


class UserFleetAssignmentSerializer(serializers.ModelSerializer):
    type_entity_object = serializers.SerializerMethodField(read_only=True)

    def get_type_entity_object(self, obj):
        if obj.type == 'machine':
            machine = Machinery.objects.filter(id=obj.object_id).first()
            if machine:
                return MachinerySerializer(machine).data

        elif obj.type == 'fleet':
            fleet = Fleet.objects.filter(id=obj.object_id).first()
            if fleet:
                return FleetSerializer(fleet).data

        else:
            return {}

    class Meta:
        model = UserFleetAssignment
        fields = ('id', 'user', 'assignment_type', 'start_date', 'end_date', 'approved', 'status', 'type',
                  'object_id', 'type_entity_object')
