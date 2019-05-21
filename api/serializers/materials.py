from rest_framework.serializers import ModelSerializer

from api.models.materials import Material, UsedMaterial


class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = ('id', 'name', 'workspace', 'measurement', 'unit_cost', 'created', 'running_out', 'quantity')


class UsedMaterialSerializer(ModelSerializer):
    class Meta:
        model = UsedMaterial
        fields = ('id', 'object_id', 'object_type', 'created', 'material', 'quantity')
