
from rest_framework import serializers

from api.models.sitestatuses import Sitestatus


class SitestatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitestatus
        fields = ('id', 'site', 'current_status', 'user')