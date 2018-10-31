from rest_framework import serializers

from api.models.fleets import Fleet


class FleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fleet
        fields = ('id', 'name', 'vehicle_type', 'uuid', 'humanUuid', 'status', 'workspace', 'created')
