from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User, Site


class Metric(TimeStampedModel):
    team = models.CharField(max_length=150)
    action = models.CharField(max_length=50)
    min_time = models.IntegerField(null=True, blank=True)
    max_time = models.IntegerField(null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)


class UserPerformanceMetric(TimeStampedModel):
    user = models.ForeignKey(to=User, null=True, blank=True, on_delete=models.CASCADE)
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
    metric = models.ForeignKey(to=Metric, null=True, blank=True, on_delete=models.CASCADE)
    points = models.IntegerField()
