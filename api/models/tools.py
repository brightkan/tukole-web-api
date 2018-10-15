from django.db import models
from api.models.tools_types import Tools_types

# Create your models here.

class Tools(models.Model):
    name = models.CharField(max_length=50,null=True)
    type = models.ForeignKey(Tools_types, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=50,null=True)
    humanUuid = models.CharField(max_length=50,null=True)
	
