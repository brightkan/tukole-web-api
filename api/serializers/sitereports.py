	
from rest_framework import serializers

from api.models.sitereports import Sitereport


class SitereportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitereport
        fields = ('id', 'site', 'user', 'report', 'workspace', 'created')
