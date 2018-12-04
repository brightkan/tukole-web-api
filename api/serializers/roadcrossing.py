from rest_framework import serializers

from api.models.roadcrossing import RoadCrossing


class RoadCrossingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadCrossing
        fields = ('id', 'distance_crossed', 'tool', 'site', 'user', 'created')
