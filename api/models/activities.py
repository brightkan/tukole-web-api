from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Site, User


class Activity(TimeStampedModel):
    site = models.ForeignKey(to=Site, related_name="activity_site", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(to=User, related_name="activity_user", on_delete=models.CASCADE, null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.BigIntegerField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
