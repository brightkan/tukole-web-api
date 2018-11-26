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
