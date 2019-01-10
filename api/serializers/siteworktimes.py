from rest_framework import serializers

from api.models import SiteArrivalTime, SiteWorkStatus, SiteCompletedWorks
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
        site_id = validated_data['site']
        user_id = validated_data['user']
        work_status = validated_data['work_status']
        reason = validated_data.get('reason', None)
        site_role_ = Siterole.objects.filter(user_id=user_id, site_id=site_id).first()
        if site_role_:
            return SiteWorkStatus.objects.create(site_role_id=site_role_.id, work_status=work_status, reason=reason)
        else:
            return {}


class SiteCompletedWorksSerializer(serializers.ModelSerializer):
    site = serializers.CharField(write_only=True)
    user = serializers.CharField(write_only=True)
    site_role = serializers.CharField(read_only=True)

    class Meta:
        model = SiteCompletedWorks
        fields = ('site_role', 'completed', 'site', 'user')

    def create(self, validated_data):
        site_id = validated_data['site']
        user_id = validated_data['user']
        site_role_ = Siterole.objects.filter(user_id=user_id, site_id=site_id).first()
        if site_role_:
            return SiteCompletedWorks.objects.create(site_role_id=site_role_.id, completed=True)
        else:
            return {}
