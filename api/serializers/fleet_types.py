from rest_framework import serializers

from api.models.fleet_types import FleetType


class FleetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetType
        fields = ('id','type','description','created','workspace')
