from rest_framework import serializers

from api.models import Incident


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ('id', 'title', 'description', 'created', 'type', 'site', 'user', 'image')
