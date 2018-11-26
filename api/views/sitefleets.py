from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from api.models import User, Site
from api.models.sitefleets import Sitefleet, UserSiteFleet
from api.serializers.fleets import FleetSerializer
from api.serializers.sitefleets import SitefleetSerializer, UserSitefleetSerializer, UserSiteFleetRequestSerializer


class SitefleetViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SitefleetSerializer
    queryset = Sitefleet.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site', 'fleet')


class UserSitefleetViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSitefleetSerializer
    queryset = UserSiteFleet.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'site_fleet')

    @action(methods=['post'], detail=False, url_path='fleet', url_name="user-site-fleet",
            serializer_class=UserSiteFleetRequestSerializer)
    def get_fleet(self, request):
        user_ = request.data['user']
        site_ = request.data['site']
        user = User.objects.filter(id=user_).first()
        site = Site.objects.filter(id=site_).first()
        fleet_ = UserSiteFleet.objects.filter(user=user, site_fleet__site=site).first()
        if fleet_:
            fleet_data = FleetSerializer(fleet_.site_fleet.fleet).data
            return Response(data=fleet_data, status=HTTP_200_OK)
        else:
            fleet_data = {"status": False, "message": "No fleet found"}
            return Response(data=fleet_data, status=HTTP_200_OK)
