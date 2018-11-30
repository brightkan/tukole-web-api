from rest_framework import serializers

from api.models.reinstallation import ReInstallation


class ReInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReInstallation
        fields = ('id', 'site', 'material', 'type', 'amount', 'user')
