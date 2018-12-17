from django.db import models
from model_utils.models import TimeStampedModel


class RepairHistory(TimeStampedModel):
    type_choices = (
        ('assignment', 'Assignment'),
        ('fault_fix', 'Fault Fix'),
    )

    fleet_type_choices = (
        ('fleet', 'Fleet'),
        ('machinery', 'Machinery'),
        ('tool', 'tool'),
    )
    type = models.CharField(choices=type_choices, max_length=255)
    reason = models.TextField()
    cost = models.IntegerField(null=True, blank=True)
    fleet = models.IntegerField()
    fleet_type = models.CharField(choices=fleet_type_choices, max_length=255)
