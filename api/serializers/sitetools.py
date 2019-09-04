from rest_framework import serializers

from api.models.sitetools import Sitetool


class SitetoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitetool
        fields = ('id', 'tool', 'site', 'user')
