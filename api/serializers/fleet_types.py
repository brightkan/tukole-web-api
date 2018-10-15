from rest_framework import serializers
from api.models.fleet_types import Fleet_types

class Fleet_typesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fleet_types
        fields = ('id', 'type', 'description')







		