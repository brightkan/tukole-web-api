from rest_framework import serializers

from api.models.history import FleetHistory, MachineHistory, ToolHistory


class FleetHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetHistory
        fields = ('id', 'fleet', 'user', 'history_type', 'time_to_fix', 'created', 'site')


class MachineHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineHistory
        fields = ('id', 'machine', 'user', 'history_type', 'time_to_fix', 'created', 'site')


class ToolHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolHistory
        fields = ('id', 'tool', 'user', 'history_type', 'time_to_fix', 'created', 'site')
