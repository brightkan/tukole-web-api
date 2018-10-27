from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User
from api.models.sites import Site 
 #,Role

# Create your models here.

class Siterole(TimeStampedModel):
    site  = models.ForeignKey(Site, on_delete=models.CASCADE, null=True, blank=True,related_name="siteroles_site")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="siteroles_user")
    #userrole = models.ForeignKey(Tool, on_delete=models.CASCADE, null=True, blank=True,related_name="Sitetools_tool")                            							  
