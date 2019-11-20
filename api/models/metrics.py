from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User, Site


class Metric(TimeStampedModel):
    metric_type_choices = (
        ('manual', 'Manual'),
        ('system', 'System')
    )
    team = models.CharField(max_length=150)
    action = models.CharField(max_length=150)
    type = models.CharField(max_length=150, choices=metric_type_choices, null=True, blank=True)


class MetricResult(TimeStampedModel):
    metric = models.ForeignKey(to=Metric, null=True, blank=True, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    time = models.DurationField(null=True, blank=True)
    points = models.IntegerField(default=0)


class UserPerformanceMetric(TimeStampedModel):
    user = models.ForeignKey(to=User, null=True, blank=True, on_delete=models.CASCADE)
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
    metric_result = models.ForeignKey(to=MetricResult, null=True, blank=True, on_delete=models.CASCADE)


class UserMetricLog(TimeStampedModel):
    user = models.ForeignKey(to=User, null=True, blank=True, on_delete=models.CASCADE)
    metric = models.ForeignKey(to=Metric, null=True, blank=True, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

