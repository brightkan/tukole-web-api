from rest_framework import serializers

from api.models import Trip
from api.models.trips import RouteChange, Other


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'start', 'start_lat', 'start_long', 'destination',
                  'destination_lat', 'destination_long', 'site_fleet', 'reason',
                  'reason_for_cancellation', 'cancelled')


class RouteChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteChange
        fields = ('id', 'created', 'site', 'user', 'route_change_reason')


class OtherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Other
        fields = ('id', 'created', 'site', 'user', 'reason')
