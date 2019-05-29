from rest_framework import serializers

from api.models import FleetCheckListItem, FleetCheckList, FleetCheckListItemResult


class FleetCheckListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetCheckListItem
        fields = ('id', 'name', 'workspace')


class FleetCheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetCheckList
        fields = ('id', 'fleet', 'user', 'workspace', 'fleet_check_list_item', 'status')


class FleetCheckListItemResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetCheckListItemResult
        fields = '__all__'


class FleetCheckResultCreateSerializer(serializers.Serializer):
    status = serializers.CharField()
    request_object_id = serializers.CharField()
    check_list_items = serializers.CharField()
