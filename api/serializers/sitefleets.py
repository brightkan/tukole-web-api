from rest_framework import serializers

from api.models.sitefleets import Sitefleet, UserSiteFleet


class SitefleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitefleet
        fields = ('id', 'site', 'fleet', 'created')


class UserSitefleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSiteFleet
        fields = ('id', 'user', 'site_fleet', 'created')


class UserSiteFleetRequestSerializer(serializers.Serializer):
    user = serializers.CharField()
    site = serializers.CharField()


class UserSiteFleetHistorySerializer(serializers.ModelSerializer):
    user_full_name = serializers.SerializerMethodField(read_only=True)
    fleet = serializers.SerializerMethodField(read_only=True)

    def get_user_full_name(self, obj):
        return "%s %s" % (obj.user.first_name, obj.user.last_name)

    def get_fleet(self, obj):
        return obj.site_fleet.fleet.name

    class Meta:
        model = UserSiteFleet
        fields = ('id', 'user', 'user_full_name', 'site_fleet', 'fleet', 'created')
