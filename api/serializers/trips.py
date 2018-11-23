from rest_framework import serializers

from api.models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'start', 'destination', 'site_fleet', 'reason')
