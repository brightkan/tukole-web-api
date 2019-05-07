from rest_framework import serializers

from api.models import Fuel, FleetFuelRequest, FuelReceipt, Machinery, Fleet
from api.serializers.fleets import FleetSerializer
from api.serializers.machinery import MachinerySerializer


class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ('id', 'fleet', 'cost', 'litres', 'mileage', 'fueled_by', 'created')


class FleetFuelRequestSerializer(serializers.ModelSerializer):
    type_entity_object = serializers.SerializerMethodField(read_only=True)

    def get_type_entity_object(self, obj):
        if obj.type == 'machine':
            machine = Machinery.objects.filter(humanUuid=obj.humanUuid).first()
            if machine:
                return MachinerySerializer(machine).data

        elif obj.type == 'fleet':
            fleet = Fleet.objects.filter(humanUuid=obj.humanUuid).first()
            if fleet:
                return FleetSerializer(fleet).data

        else:
            return {}

    class Meta:
        model = FleetFuelRequest
        fields = ('id', 'object_id', 'user', 'requested_fuel_in_litres', 'received_fuel_in_litres',
                  'mileage_at_fuelling_time', 'status', 'refuel_reject_reason', 'created', 'approved',
                  'pump_screenshot', 'type', 'type_entity_object', 'allow_full_tank', 'humanUuid',
                  'fuelled_by', 'approved_by', 'received_amount', 'approved_amount', 'object_type'
                  )


class FuelReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelReceipt
        fields = ('id', 'fleet', 'user', 'fuel_in_litres', 'total_fuel')


class FuelReceiptSummarySerializer(serializers.Serializer):
    type = serializers.CharField()
    month = serializers.DateTimeField()
