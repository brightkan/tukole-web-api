from rest_framework import serializers

from api.models.siteroles import Siterole
from api.models.sites import Site, SiteImage, SiteDocument, SitePIP, SitePower


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = (
            'id', 'site_name', 'site_deleted', 'site_accessible', 'site_surveyed', 'location_lat',
            'location_long', 'start_date', 'survey_date', 'expected_end_date', 'clientId',
            'current_stage', 'archivedStatus', 'workspace', 'surveyor', 'ackStatus', 'ack_user',
            'ack_date', 'survay_time', 'created', 'modified', 'can_client_view_survey_reports', 'site_contact_person',
            'site_contact_phone_number', 'site_location', 'site_accepted', 'company', 'site_connected',
            'site_connection_date', 'site_connection_request_acknowledged', 'site_ready_for_connection',
            'number_of_site_fleet', 'number_of_members_on_site', 'site_image', 'site_completed',
            'isp_works_complete', 'osp_works_complete', 'ofc_works_complete', 'site_powering_complete',
            'original_trenching_distance', 'current_trenching_distance', 'site_drawing', 'site_address',
            'site_usd_rate',
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
            'ack_date', 'survay_time', 'created', 'modified', 'can_client_view_survey_reports', 'site_contact_person',
            'site_contact_phone_number', 'site_location', 'site_accepted', 'company', 'site_connected',
            'site_connection_date', 'site_connection_request_acknowledged', 'site_ready_for_connection',
            'number_of_site_fleet', 'number_of_members_on_site', 'site_image', 'site_completed',
            'isp_works_complete', 'osp_works_complete', 'ofc_works_complete', 'site_powering_complete',
            'original_trenching_distance', 'current_trenching_distance', 'site_drawing', 'site_address',
            'site_usd_rate', 'user_role'
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


class SitePowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SitePower
        fields = ('id', 'end_time', 'start_time', 'material_used', 'user', 'type', 'site',)
