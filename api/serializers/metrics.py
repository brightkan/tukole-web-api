from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Metric, UserPerformanceMetric
from api.models.metrics import MetricResult, UserMetricLog
from api.serializers.sites import SiteSerializer
from api.serializers.users import UserSerializer


class MetricSerializer(ModelSerializer):
    class Meta:
        model = Metric
        fields = ('id', 'team', 'action', 'created', 'type')


class UserPerformanceMetricSerializer(ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = UserSerializer(instance.user).data
        data['metric'] = MetricSerializer(instance.metric).data
        return data

    class Meta:
        model = UserPerformanceMetric
        fields = ('id', 'user', 'metric_result', 'points', 'created')


class GetPointFromMetricSerializer(serializers.Serializer):
    team = serializers.CharField()
    action = serializers.CharField()
    min_time = serializers.CharField()
    max_time = serializers.CharField()


class MetricResultSerializer(ModelSerializer):
    class Meta:
        model = MetricResult
        fields = ('id', 'metric', 'start_time', 'end_time', 'time', 'created')


class UserMetricLogSerializer(ModelSerializer):
    class Meta:
        model = UserMetricLog
        fields = ('id', 'user', 'metric', 'start_time', 'end_time', 'created')
