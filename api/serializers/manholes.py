from rest_framework import serializers

from api.models import ManHole, ManHoleAssignment, ManHoleDuration
from api.models.manholes import ManHoleInstallation


class ManHoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManHole
        fields = ('id', 'site', 'number', 'created')


class ManHoleLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManHoleDuration
        fields = ('id', 'manhole', 'start_time', 'end_time', 'user', 'created')


class ManHoleCreateAssignmentSerializer(serializers.Serializer):
    user = serializers.CharField()
    manhole = serializers.CharField()


class ManHoleUserFilterSerializer(serializers.Serializer):
    user = serializers.CharField()


class ManHoleAssignmentSerializer(serializers.ModelSerializer):
    login_time = serializers.SerializerMethodField(read_only=True)
    logout_time = serializers.SerializerMethodField(read_only=True)

    def get_login_time(self, obj):
        manhole_duration = ManHoleDuration.objects.filter(user=obj.user, manhole=obj.manhole).first()
        if manhole_duration:
            return manhole_duration.start_time
        else:
            return ""

    def get_logout_time(self, obj):
        manhole_duration = ManHoleDuration.objects.filter(user=obj.user, manhole=obj.manhole).first()
        if manhole_duration:
            return manhole_duration.end_time
        else:
            return ""

    class Meta:
        model = ManHoleAssignment
        fields = ('id', 'user', 'manhole', 'login_time', 'logout_time', 'created')


class ManHoleInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManHoleInstallation
        fields = ('id', 'site', 'user', 'number_installed', 'created')


class HandHoleInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManHoleInstallation
        fields = ('id', 'site', 'user', 'number_installed', 'created')
