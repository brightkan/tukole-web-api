from rest_framework import serializers

from api.models import SiteArrivalTime, SiteWorkStatus
from api.models.siteroles import Siterole


class SiteArrivalTimeSerializer(serializers.ModelSerializer):
    site = serializers.CharField(write_only=True)
    user = serializers.CharField(write_only=True)
    site_role = serializers.CharField(read_only=True)

    class Meta:
        model = SiteArrivalTime
        fields = ('site_role', 'arrival_time', 'site', 'user')

    def create(self, validated_data):
        site_id = validated_data['site']
        user_id = validated_data['user']
        arrival_time = validated_data['arrival_time']
        site_role_ = Siterole.objects.filter(user_id=user_id, site_id=site_id).first()
        if site_role_:
            return SiteArrivalTime.objects.create(site_role_id=site_role_.id, arrival_time=arrival_time)
        else:
            return {}


class SiteWorkStatusSerializer(serializers.ModelSerializer):
    site = serializers.CharField(write_only=True)
    user = serializers.CharField(write_only=True)
    site_role = serializers.CharField(read_only=True)

    class Meta:
        model = SiteWorkStatus
        fields = ('site_role', 'work_status', 'reason', 'site', 'user')

    def create(self, validated_data):
        return super().create(validated_data)


class SiteCompletedWorksSerializer(serializers.ModelSerializer):
    site = serializers.CharField(write_only=True)
    user = serializers.CharField(write_only=True)
    site_role = serializers.CharField(read_only=True)

    class Meta:
        model = SiteArrivalTime
        fields = ('site_role', 'completed', 'site', 'user')
