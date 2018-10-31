 
from rest_framework import serializers

from api.models.sitefleets import Sitefleet


class SitefleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitefleet
        fields = ('id', 'site', 'fleet', 'created')
