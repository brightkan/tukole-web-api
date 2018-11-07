from rest_framework import serializers

from api.models.warehousematerials import WarehouseMaterial


class WarehouseMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseMaterial
        fields = ('id', 'site', 'is_returned', 'material','quantity','created')															  