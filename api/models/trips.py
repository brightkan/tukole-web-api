from django.db import models
from model_utils.models import TimeStampedModel

from api.models.sitefleets import Sitefleet


class Trip(TimeStampedModel):
    start = models.CharField(max_length=255, null=True, blank=True)
    start_long = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    start_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    destination = models.CharField(max_length=255, null=True, blank=True)
    destination_long = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    destination_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    site_fleet = models.ForeignKey(to=Sitefleet, null=True, blank=True, on_delete=models.CASCADE)
