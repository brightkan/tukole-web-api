from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Workspace
from api.models.fleet_types import FleetType


# Create your models here.

class Fleet(TimeStampedModel):
    status_choices = (
        ('available', 'available'),
        ('broken_down', 'broken_down'),
        ('assigned', 'assigned')
    )
    name = models.CharField(max_length=50, null=True)
    vehicle_type = models.ForeignKey(to=FleetType, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name="fleet_vehicle_type")
    uuid = models.CharField(max_length=50, null=True)
    humanUuid = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=150, null=True, choices=status_choices)
    workspace = models.ForeignKey(to=Workspace, on_delete=models.CASCADE, null=True, blank=True,
                                  related_name="fleet_workspace")
