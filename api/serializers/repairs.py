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
        fields = '__all__'
