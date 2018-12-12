from rest_framework import serializers

from api.models.siteroles import Siterole
from api.models.sites import Site, SiteImage


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = (
            'id', 'site_name', 'site_deleted', 'site_accessible', 'site_surveyed', 'location_lat',
            'location_long', 'start_date', 'survey_date', 'expected_end_date', 'clientId',
            'current_stage', 'archivedStatus', 'workspace', 'surveyor', 'ackStatus', 'ack_user',
            'ack_date', 'survay_time', 'created', 'modified'
        )


class SiteUserRoleSerializer(serializers.ModelSerializer):
    user_role = serializers.SerializerMethodField()

    def get_user_role(self, obj):
        request = getattr(self.context, 'request', None)
        if request:
            user = request.user
            site_role = Siterole.objects.filter(user=user, site=obj).first()
            if site_role:
                return site_role.role
        else:
            return ""

    class Meta:
        model = Site
        fields = (
            'id', 'site_name', 'site_deleted', 'site_accessible', 'site_surveyed', 'location_lat',
            'location_long', 'start_date', 'survey_date', 'expected_end_date', 'clientId',
            'current_stage', 'archivedStatus', 'workspace', 'surveyor', 'ackStatus', 'ack_user',
            'ack_date', 'survay_time', 'created', 'modified', 'user_role'
        )


class SiteImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteImage
        fields = ('id', 'site', 'image', 'status', 'created', 'modified')
