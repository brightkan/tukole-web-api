from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from api.models import Metric, UserPerformanceMetric
from api.serializers.metrics import (
    MetricSerializer,
    UserPerformanceMetricSerializer,
    GetPointFromMetricSerializer,
)


class MetricViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MetricSerializer
    queryset = Metric.objects.all()

    @action(
        methods=['post'],
        detail=False,
        url_path='get-points',
        url_name="get-points",
        serializer_class=GetPointFromMetricSerializer,
    )
    def get_points(self, request):
        team = request.data['team']
        action = request.data['action']
        min_time = request.data['min_time']
        max_time = request.data['max_time']
        metric = Metric.objects.filter(
            team=team, action=action, min_time__lte=min_time, max_time__gte=max_time
        ).first()
        if metric:
            data = MetricSerializer(metric).data
            return Response(data=data, status=HTTP_200_OK)
        else:
            return {}


class UserPerformanceMetricViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserPerformanceMetricSerializer
    queryset = UserPerformanceMetric.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'metric', 'site')
