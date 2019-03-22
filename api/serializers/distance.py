from rest_framework import serializers

from api.models.distance import TrenchedDistance


class TrenchedDistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrenchedDistance
        fields = ('id', 'site', 'user', 'distance', 'depth', 'created', 'fm_approved')
