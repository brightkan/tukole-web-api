from rest_framework import serializers

from api.models import ManHole, ManHoleAssignment


class ManHoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManHole
        fields = ('id', 'site', 'number', 'created')


class ManHoleLoginSerializer(serializers.Serializer):
    manhole = serializers.CharField()
    duration = serializers.CharField()
    user = serializers.CharField()


class ManHoleCreateAssignmentSerializer(serializers.Serializer):
    user = serializers.CharField()
    manhole = serializers.CharField()


class ManHoleAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManHoleAssignment
        fields = ('id', 'user', 'manhole', 'created')
