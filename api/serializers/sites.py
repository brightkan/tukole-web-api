from rest_framework import serializers

from api.models.sites import Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = (
            'id', 'site_name', 'location_lat', 'location_long', 'start_date', 'survey_date',
            'expected_end_date', 'archivedStatus', 'site_surveyed', 'site_accessible', 'clientId', 'ackStatus',
            'current_stage', 'archivedStatus', 'workspace', 'created', 'modified',)
