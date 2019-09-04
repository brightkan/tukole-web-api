from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Metric, UserPerformanceMetric
from api.serializers.sites import SiteSerializer
from api.serializers.users import UserSerializer


class MetricSerializer(ModelSerializer):
    class Meta:
        model = Metric
        fields = ('id', 'team', 'action', 'min_time', 'max_time', 'created', 'points')


class UserPerformanceMetricSerializer(ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['site'] = SiteSerializer(instance.site).data
        data['user'] = UserSerializer(instance.user).data
        data['metric'] = MetricSerializer(instance.metric).data
        return data

    class Meta:
        model = UserPerformanceMetric
        fields = ('id', 'user', 'site', 'metric', 'points', 'created')


class GetPointFromMetricSerializer(serializers.Serializer):
    team = serializers.CharField()
    action = serializers.CharField()
    min_time = serializers.CharField()
    max_time = serializers.CharField()
