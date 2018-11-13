from rest_framework import serializers

from api.models.sites import Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = (
            'id','site_name' ,'site_deleted' ,'site_accessible', 'site_surveyed', 'location_lat', 
            'location_long', 'start_date', 'survey_date','expected_end_date', 'clientId', 
            'current_stage', 'archivedStatus', 'workspace','surveyor', 'ackStatus', 'ack_user',
            'ack_date', 'created', 'modified'
	      )

			
	 