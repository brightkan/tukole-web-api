from rest_framework import serializers

from api.models.siteroles import Siterole
from api.models.sites import Site, SiteImage, SiteDocument, SitePIP, SitePower
from api.serializers.company import CompanySerializer
from api.serializers.users import UserSerializer


class SiteSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['client_object'] = UserSerializer(instance.clientId).data
        context['company_object'] = CompanySerializer(instance.company).data
        return context

    class Meta:
        model = Site
        fields = (
            'id',
            'site_name',
            'site_deleted',
            'site_accessible',
            'site_surveyed',
            'location_lat',
            'location_long',
            'start_date',
            'survey_date',
            'expected_end_date',
            'clientId',
            'current_stage',
            'archivedStatus',
            'workspace',
            'surveyor',
            'ackStatus',
            'ack_user',
            'ack_date',
            'survay_time',
            'created',
            'modified',
            'can_client_view_survey_reports',
            'site_contact_person',
            'site_contact_phone_number',
            'site_location',
            'site_accepted',
            'company',
            'site_connected',
            'site_connection_date',
            'site_connection_request_acknowledged',
            'site_ready_for_connection',
            'number_of_site_fleet',
            'number_of_members_on_site',
            'site_image',
            'site_completed',
            'isp_works_complete',
            'osp_works_complete',
            'ofc_works_complete',
            'site_powering_complete',
            'original_trenching_distance',
            'current_trenching_distance',
            'site_drawing',
            'site_address',
            'site_usd_rate',
            'site_type',
        )


class SiteUserRoleSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['client_object'] = UserSerializer(instance.clientId).data
        context['company_object'] = CompanySerializer(instance.company).data
        return context

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
            'id',
            'site_name',
            'site_deleted',
            'site_accessible',
            'site_surveyed',
            'location_lat',
            'location_long',
            'start_date',
            'survey_date',
            'expected_end_date',
            'clientId',
            'current_stage',
            'archivedStatus',
            'workspace',
            'surveyor',
            'ackStatus',
            'ack_user',
            'ack_date',
            'survay_time',
            'created',
            'modified',
            'can_client_view_survey_reports',
            'site_contact_person',
            'site_contact_phone_number',
            'site_location',
            'site_accepted',
            'company',
            'site_connected',
            'site_connection_date',
            'site_connection_request_acknowledged',
            'site_ready_for_connection',
            'number_of_site_fleet',
            'number_of_members_on_site',
            'site_image',
            'site_completed',
            'isp_works_complete',
            'osp_works_complete',
            'ofc_works_complete',
            'site_powering_complete',
            'original_trenching_distance',
            'current_trenching_distance',
            'site_drawing',
            'site_address',
            'site_usd_rate',
            'user_role',
            'site_type',
            'site_is_being_worked',
        )


class SiteImageSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return_data = super().to_representation(instance)
        return_data['user'] = UserSerializer(instance.user).data
        return return_data

    class Meta:
        model = SiteImage
        fields = ('id', 'site', 'image', 'status', 'created', 'modified', 'long', 'lat', 'user')


class SiteDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteDocument
        fields = ('id', 'site', 'file', 'title', 'created', 'modified')


class SitePIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = SitePIP
        fields = ('id', 'site', 'task', 'start', 'end', 'pip_upload', 'created', 'modified')


class SitePowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SitePower
        fields = (
            'id',
            'end_time',
            'start_time',
            'material_used',
            'user',
            'type',
            'site',
            'powering_successful',
            'product',
            'comment',
            'equipment_used',
        )
