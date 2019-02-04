from rest_framework import serializers

from api.models import Fuel, FleetFuelRequest


class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ('id', 'fleet', 'cost', 'litres', 'mileage', 'fueled_by', 'created')


class FleetFuelRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetFuelRequest
        fields = ('id', 'fleet', 'user', 'requested_fuel_in_litres', 'received_fuel_in_litres', 'total_fuel_amount',
                  'mileage_at_fuelling_time', 'status', 'refuel_reject_reason', 'created')
