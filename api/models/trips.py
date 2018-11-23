from django.db import models
from model_utils.models import TimeStampedModel

from api.models.sitefleets import Sitefleet


class Trip(TimeStampedModel):
    start = models.DecimalField(max_digits=9, decimal_places=6)
    destination = models.DecimalField(max_digits=9, decimal_places=6)
    reason = models.TextField(null=True, blank=True)
    site_fleet = models.ForeignKey(to=Sitefleet, null=True, blank=True, on_delete=models.CASCADE)
