from rest_framework import serializers

from api.models import ManHole


class ManHoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManHole
        fields = ('id', 'site', 'number', 'created')


class ManHoleLoginSerializer(serializers.Serializer):
    manhole = serializers.CharField()
    duration = serializers.CharField()
    user = serializers.CharField()
