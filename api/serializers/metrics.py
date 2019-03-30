from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Metric, UserPerformanceMetric


class MetricSerializer(ModelSerializer):
    class Meta:
        model = Metric
        fields = ('id', 'team', 'action', 'min_time', 'max_time', 'created', 'points')


class UserPerformanceMetricSerializer(ModelSerializer):
    class Meta:
        model = UserPerformanceMetric
        fields = ('id', 'user', 'site', 'metric', 'points', 'created')


class GetPointFromMetricSerializer(serializers.Serializer):
    team = serializers.CharField()
    action = serializers.CharField()
    min_time = serializers.CharField()
    max_time = serializers.CharField()
