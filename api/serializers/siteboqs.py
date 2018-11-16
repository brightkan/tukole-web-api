from rest_framework import serializers

from api.models import Material
from api.models.siteboqs import Siteboq


class SiteboqSerializer(serializers.ModelSerializer):
    material_name = serializers.SerializerMethodField()
    material_measurement = serializers.SerializerMethodField()
    material_unit_cost = serializers.SerializerMethodField()

    def get_material_name(self):
        material = Material.objects.filter(id=self.material).first()
        if material:
            return material.name
        else:
            return ""

    def get_material_measurement(self):
        material = Material.objects.filter(id=self.material).first()
        if material:
            return material.measurement
        else:
            return ""

    def get_material_unit_cost(self):
        material = Material.objects.filter(id=self.material).first()
        if material:
            return material.unit_cost
        else:
            return ""

    class Meta:
        model = Siteboq
        fields = ('id', 'site', 'material', 'material_name', 'material_measurement', 'material_unit_cost',
                  'actual_quantity', 'estimate_quantity', 'boq_type', 'user', 'created')
