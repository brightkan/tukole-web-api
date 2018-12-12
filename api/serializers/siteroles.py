from rest_framework import serializers

from api.models.siteroles import Siterole


class SiteroleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siterole
        fields = ('id', 'site', 'user', 'created', 'role')
