from django.db import models
from model_utils.models import TimeStampedModel

from api.models.machinery import Machinery
from api.models.sites import Site


# Create your models here.

class SiteMachines (TimeStampedModel):
    site  = models.ForeignKey(Site, on_delete=models.CASCADE, null=True, blank=True,related_name="sitemachines_site")
    machine = models.ForeignKey(Machinery, on_delete=models.CASCADE, null=True, blank=True, related_name="sitemachines_machine")
	

