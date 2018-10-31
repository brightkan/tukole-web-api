	
from rest_framework import serializers

from api.models.machinery_types import MachineryType


class MachineryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineryType
        fields = ('id', 'type', 'description', 'created')

