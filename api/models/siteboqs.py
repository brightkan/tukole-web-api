from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User
from api.models.sites import Site
from api.models.materials import Material



# Create your models here.

class Siteboq (TimeStampedModel):
    site  = models.ForeignKey(Site, on_delete=models.CASCADE, null=True, blank=True,related_name="siteboq_site")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=True, blank=True, related_name="siteboq_material")
    quantity = models.CharField(max_length=50, null=True)
    boq_type = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="siteboq_user")
    
	
