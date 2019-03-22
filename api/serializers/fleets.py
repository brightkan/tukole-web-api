from rest_framework import serializers

from api.models.fleets import Fleet, UserFleetAssignment


class FleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fleet
        fields = ('id', 'name', 'vehicle_type', 'uuid', 'humanUuid', 'status', 'workspace', 'created')


class UserFleetAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFleetAssignment
        fields = ('id', 'user', 'fleet', 'assignment_type', 'start_date', 'end_date', 'approved')
