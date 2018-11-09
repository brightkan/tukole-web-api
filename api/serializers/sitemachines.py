
from rest_framework import serializers

from api.models.sitemachines import SiteMachines


class SiteMachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteMachines
        fields = ('id', 'site', 'machine', 'created')
