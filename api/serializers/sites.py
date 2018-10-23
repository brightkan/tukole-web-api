from rest_framework import serializers

from api.models.sites import Sites


class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = (
            'id', 'site_name', 'location_lat', 'location_long', 'start_date', 'expected_end_date', 'archivedStatus',
            'clientId', 'ackStatus', 'current_stage', 'archivedStatus', 'workspace', 'created', 'updated')
