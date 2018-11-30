from rest_framework import serializers

from api.models import Cost


class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = ('id', 'site', 'user', 'name', 'value')
