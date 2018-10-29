from rest_framework import serializers

from api.models.machinery import Machinery


class MachinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Machinery
        fields = ('id', 'name', 'uuid', 'humanUuid', 'status','workspace')
