from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models import SiteArrivalTime, SiteWorkStatus, SiteCompletedWorks
from api.serializers.siteworktimes import SiteArrivalTimeSerializer, SiteWorkStatusSerializer, \
    SiteCompletedWorksSerializer


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
    filter_fields = ('site_role',)


class SiteCompletedWorksViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SiteCompletedWorksSerializer
    queryset = SiteCompletedWorks.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site_role',)
