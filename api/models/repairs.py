from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User


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
    fm_approved = models.BooleanField(null=True, blank=True)


class RepairTicket(TimeStampedModel):
    type_choices = (
        ('machine', 'Machine'),
        ('tool', 'Tool'),
        ('fleet', 'Fleet'),
    )
    reported_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    time_reported = models.DateTimeField(null=True, blank=True)
    time_acknowledged = models.DateTimeField(null=True, blank=True)
    acknowledged_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    assessment = models.CharField(max_length=255, null=True, blank=True)
    requisition_materials = models.CharField(max_length=255, null=True, blank=True)
    requisition_started = models.DateTimeField(null=True, blank=True)
    requisition_ended = models.DateTimeField(null=True, blank=True)
    repairs_complete = models.BooleanField(null=True, blank=True)
    repairs_complete_timestamp = models.DateTimeField(null=True, blank=True)
    mechanic = models.ForeignKey(to=User, on_delete=models.CASCADE)
    supervised_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    type = models.CharField(choices=type_choices)
    object_id = models.IntegerField(null=True, blank=True)
