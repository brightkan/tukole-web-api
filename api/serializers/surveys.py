	
from rest_framework import serializers

from api.models.surveys import Survey


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'creator', 'site_name', 'coordinates_lat', 'coordinates_long', 'surveyor', 'ack','ack_user','created')
		
		