from django.db import models
from model_utils.models import TimeStampedModel

from api.models.fleet_types import Fleet_types


# Create your models here.

class Fleet(TimeStampedModel):
    name = models.CharField(max_length=50, null=True)
    vehicle_type = models.ForeignKey(Fleet_types, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=50, null=True)
    humanUuid = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
