from rest_framework import serializers

from api.models import ManHole, ManHoleAssignment, ManHoleDuration
from api.models.manholes import (
    ManHoleInstallation,
    ODFInstallation,
    ODFTermination,
    DuctInstallation,
    CableInstallation,
    Trunking,
    ODFTerminationTool)
from api.models.tools import Tool
from api.serializers.tools import ToolSerializer


class ManHoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManHole
        fields = ('id', 'site', 'number', 'created')


class ManHoleLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManHoleDuration
        fields = (
            'id',
            'manhole',
            'start_time',
            'end_time',
            'user',
            'created',
            'to_fibers',
            'to_tube',
            'from_fibers',
            'from_tube',
        )


class ManHoleCreateAssignmentSerializer(serializers.Serializer):
    user = serializers.CharField()
    manhole = serializers.CharField()


class ManHoleUserFilterSerializer(serializers.Serializer):
    user = serializers.CharField()


class ManHoleUserImportSerializer(serializers.Serializer):
    file = serializers.FileField()
    site = serializers.IntegerField(required=False)
    user_assigned = serializers.IntegerField()


class ManHoleImportSerializer(serializers.Serializer):
    file = serializers.FileField()
    site = serializers.IntegerField(required=False)


class ManHoleAssignmentSerializer(serializers.ModelSerializer):
    login_time = serializers.SerializerMethodField(read_only=True)
    logout_time = serializers.SerializerMethodField(read_only=True)
    to_tube = serializers.SerializerMethodField(read_only=True)
    from_tube = serializers.SerializerMethodField(read_only=True)
    to_fibers = serializers.SerializerMethodField(read_only=True)
    from_fibers = serializers.SerializerMethodField(read_only=True)

    def get_login_time(self, obj):
        manhole_duration = ManHoleDuration.objects.filter(
            user=obj.user, manhole=obj.manhole
        ).first()
        if manhole_duration:
            return manhole_duration.start_time
        else:
            return ""

    def get_to_tube(self, obj):
        manhole_duration = ManHoleDuration.objects.filter(
            user=obj.user, manhole=obj.manhole
        ).first()
        if manhole_duration:
            return manhole_duration.to_tube
        else:
            return ""

    def get_from_tube(self, obj):
        manhole_duration = ManHoleDuration.objects.filter(
            user=obj.user, manhole=obj.manhole
        ).first()
        if manhole_duration:
            return manhole_duration.from_tube
        else:
            return ""

    def get_to_fibers(self, obj):
        manhole_duration = ManHoleDuration.objects.filter(
            user=obj.user, manhole=obj.manhole
        ).first()
        if manhole_duration:
            return manhole_duration.to_fibers
        else:
            return ""

    def get_from_fibers(self, obj):
        manhole_duration = ManHoleDuration.objects.filter(
            user=obj.user, manhole=obj.manhole
        ).first()
        if manhole_duration:
            return manhole_duration.from_fibers
        else:
            return ""

    def get_logout_time(self, obj):
        manhole_duration = ManHoleDuration.objects.filter(
            user=obj.user, manhole=obj.manhole
        ).first()
        if manhole_duration:
            return manhole_duration.end_time
        else:
            return ""

    class Meta:
        model = ManHoleAssignment
        fields = (
            'id',
            'user',
            'manhole',
            'login_time',
            'logout_time',
            'created',
            'fm_approved',
            'to_fibers',
            'to_tube',
            'from_fibers',
            'from_tube',
        )


class ManHoleInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManHoleInstallation
        fields = ('id', 'site', 'user', 'number_installed', 'created', 'fm_approved')


class HandHoleInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManHoleInstallation
        fields = ('id', 'site', 'user', 'number_installed', 'created', 'fm_approved')


class ODFInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ODFInstallation
        fields = ('id',
                  'site',
                  'user',
                  'created',
                  'size_of_odf',
                  'number_of_odf_installed',
                  'type_of_odfs',
                  'type_of_connectors',
                  'odf_ports_terminated',
                  'odf_ports_link',
                  'number_of_fiber_cables_terminated',
                  'odf_install_confirmed',
                  'odf_labelled_confirmed',
                  )


class ODFTerminationSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return_json = super().to_representation(instance)
        tools_ids = ODFTerminationTool.objects.filter(odf_termination=instance).values_list('tool__id', flat=True)
        tools_ids = list(tools_ids)
        tools = Tool.objects.filter(id__in=tools_ids)
        return_json['tools'] = ToolSerializer(tools, many=True).data
        return return_json

    tools = serializers.CharField(write_only=True)

    class Meta:
        model = ODFTermination
        fields = ('id', 'site', 'user', 'created', 'ports', 'client', 'label', 'cores', 'tools')


class DuctInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuctInstallation
        fields = ('id', 'site', 'user', 'created', 'number', 'size', 'micro_duct', 'duct_type')


class CableInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CableInstallation
        fields = ('id', 'site', 'user', 'created', 'length', 'size', 'method', 'type')


class TrunkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trunking
        fields = '__all__'
