from rest_framework import serializers

from api.models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'start_lat', 'start_long', 'destination_lat', 'destination_long', 'site_fleet', 'reason')
