from rest_framework import serializers

from api.models.siteboqs import Siteboq


class SiteboqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siteboq
        fields = ('id', 'site', 'material', 'actual_quantity', 'estimate_quantity', 'boq_type', 'user', 'created')
