from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Workspace, User
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


class UserFleetAssignment(TimeStampedModel):
    approve_status = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    )
    assignment_type_choices = (
        ('assignment', 'Assignment'),
        ('request', 'Request')
    )

    type_choices = (
        ('machine', 'Machine'),
        ('fleet', 'Fleet')
    )
    assignment_type = models.CharField(max_length=150, null=True, blank=True, choices=assignment_type_choices)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    fleet = models.ForeignKey(to=Fleet, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=155, choices=type_choices, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    approved = models.BooleanField(default=Fleet)
    status = models.IntegerField(choices=approve_status, default=0)
