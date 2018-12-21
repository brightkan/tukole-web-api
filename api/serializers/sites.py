from rest_framework import serializers

from api.models.siteroles import Siterole
from api.models.sites import Site, SiteImage, SiteDocument, SitePIP


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = (
            'id', 'site_name', 'site_deleted', 'site_accessible', 'site_surveyed', 'location_lat',
            'location_long', 'start_date', 'survey_date', 'expected_end_date', 'clientId',
            'current_stage', 'archivedStatus', 'workspace', 'surveyor', 'ackStatus', 'ack_user',
            'ack_date', 'survay_time', 'created', 'modified', 'can_client_view_survey_reports'
        )


class SiteUserRoleSerializer(serializers.ModelSerializer):
    user_role = serializers.SerializerMethodField()

    def get_user_role(self, obj):
        user = self.context.get('user', None)
        if user:
            site_role = Siterole.objects.filter(user_id=user, site=obj).first()
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
            'ack_date', 'survay_time', 'created', 'modified', 'user_role', 'can_client_view_survey_reports'
        )


class SiteImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteImage
        fields = ('id', 'site', 'image', 'status', 'created', 'modified')


class SiteDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteDocument
        fields = ('id', 'site', 'file', 'title', 'created', 'modified')


class SitePIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = SitePIP
        fields = ('id', 'site', 'task', 'start', 'end', 'created', 'modified')
