

	
from rest_framework import serializers
from api.models.sites import Sites

##//////////////////

class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = ('id', 'site_name', 'location','clientId', 'ackStatus', 'workStatus', 'archivedStatus','created_at', 'updated_at')	
    
