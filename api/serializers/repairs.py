from rest_framework import serializers

from api.models import RepairHistory


class RepairHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairHistory
        fields = ('id', 'type', 'reason', 'cost', 'fleet', 'fleet_type', 'created', 'fm_approved')
