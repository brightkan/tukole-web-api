from django.db import models
from model_utils.models import TimeStampedModel

from api.models.sites import Site 
from api.models.fleets import Fleet

# Create your models here.

class Sitefleet (TimeStampedModel):
    site  = models.ForeignKey(Site, on_delete=models.CASCADE, null=True, blank=True,related_name="sitefleet_site")
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE, null=True, blank=True, related_name="sitefleet_fleet")
    