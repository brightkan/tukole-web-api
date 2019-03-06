from rest_framework import serializers

from api.models import FleetCheckListItem, FleetCheckList


class FleetCheckListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetCheckListItem
        fields = ('id', 'name')


class FleetCheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetCheckList
        fields = ('id', 'fleet', 'user', 'workspace', 'fleet_check_list_item', 'status')
