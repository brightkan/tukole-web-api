from django.db import models
from model_utils.models import TimeStampedModel

from api.models.fleets import Fleet
from api.models.sites import Site


# Create your models here.

class Sitefleet(TimeStampedModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True, blank=True, related_name="sitefleet_site")
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE, null=True, blank=True, related_name="sitefleet_fleet")


class UserSiteFleet(TimeStampedModel):
    user = models.ForeignKey(Site, on_delete=models.CASCADE, null=True, blank=True, related_name="driver_site_fleet")
    site_fleet = models.ForeignKey(Sitefleet, on_delete=models.CASCADE, null=True, blank=True,
                                   related_name="site_driver_site_fleet")

    class Meta:
        unique_together = ('user', 'site_fleet')
