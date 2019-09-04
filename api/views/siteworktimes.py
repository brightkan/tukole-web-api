from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from api.models import SiteArrivalTime, SiteWorkStatus, SiteCompletedWorks, Site
from api.serializers.siteworktimes import (
    SiteArrivalTimeSerializer,
    SiteWorkStatusSerializer,
    SiteCompletedWorksSerializer,
)


class SiteArrivalTimeViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SiteArrivalTimeSerializer
    queryset = SiteArrivalTime.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site_role',)


class SiteWorkStatusViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SiteWorkStatusSerializer
    queryset = SiteWorkStatus.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site',)

    @action(methods=['get'], detail=True, url_path='current', url_name="current-site-work-status")
    def get_current_work_status(self, request, pk):
        data = {}
        site = Site.objects.filter(id=pk).first()
        if site:
            site_work_status = SiteWorkStatus.objects.filter(site=site).last()
            if site_work_status:
                data = SiteWorkStatusSerializer(site_work_status).data
        # email = request.data['email']
        # data = SiteWorkStatus(user).data
        return Response(data=data, status=HTTP_200_OK)


class SiteCompletedWorksViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SiteCompletedWorksSerializer
    queryset = SiteCompletedWorks.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site_role',)
