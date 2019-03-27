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
        model = FleetFuelRequest
        fields = ('id', 'object_id', 'user', 'requested_fuel_in_litres', 'received_fuel_in_litres',
                  'mileage_at_fuelling_time', 'status', 'refuel_reject_reason', 'created', 'approved', 'fuel_amount',
                  'pump_screenshot', 'type', 'type_entity_object'
                  )


class FuelReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelReceipt
        fields = ('id', 'fleet', 'user', 'fuel_in_litres', 'total_fuel')
