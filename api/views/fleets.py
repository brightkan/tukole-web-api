# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from api.models import UserSiteFleet
from api.models.fleets import Fleet
from api.serializers.fleets import FleetSerializer
from api.serializers.sitefleets import UserSiteFleetHistorySerializer


class FleetViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('workspace', 'vehicle_type')

    @action(methods=['get'], detail=True, url_path='history', url_name="history")
    def fleet_history(self, request, pk):
        assignments = UserSiteFleet.objects.filter(site_fleet__fleet__id=pk)

        if assignments:
            print(assignments)
            data = UserSiteFleetHistorySerializer(assignments, many=True).data
        else:
            data = {"error": "User is not attached to any site"}
        return Response(data=data, status=HTTP_200_OK)
