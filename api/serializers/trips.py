from rest_framework import serializers

from api.models import Trip
from api.models.trips import RouteChange


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'start', 'start_lat', 'start_long', 'destination',
                  'destination_lat', 'destination_long', 'site_fleet', 'reason',
                  'reason_for_cancellation', 'cancelled')


class RouteChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteChange
        fields = ('id', 'created', 'site', 'user')
