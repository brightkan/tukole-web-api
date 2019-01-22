from rest_framework import serializers

from api.models import Fuel


class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ('id', 'fleet', 'cost', 'litres', 'mileage', 'fueled_by', 'created')
