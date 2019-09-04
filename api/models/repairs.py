from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User


class RepairHistory(TimeStampedModel):
    type_choices = (('assignment', 'Assignment'), ('fault_fix', 'Fault Fix'))

    fleet_type_choices = (('fleet', 'Fleet'), ('machinery', 'Machinery'), ('tool', 'tool'))
    type = models.CharField(choices=type_choices, max_length=255)
    reason = models.TextField()
    cost = models.IntegerField(null=True, blank=True)
    fleet = models.IntegerField()
    fleet_type = models.CharField(choices=fleet_type_choices, max_length=255)
    fm_approved = models.BooleanField(null=True, blank=True)


class RepairTicket(TimeStampedModel):
    type_choices = (('machine', 'Machine'), ('tool', 'Tool'), ('fleet', 'Fleet'))
    reported_by = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="repair_reported_by", null=True, blank=True
    )
    time_reported = models.DateTimeField(null=True, blank=True)
    time_acknowledged = models.DateTimeField(null=True, blank=True)
    acknowledged_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="repair_acknowledged_by",
        null=True,
        blank=True,
    )
    assessment = models.CharField(max_length=255, null=True, blank=True)
    requisition_materials = models.CharField(max_length=255, null=True, blank=True)
    requisition_started = models.DateTimeField(null=True, blank=True)
    requisition_ended = models.DateTimeField(null=True, blank=True)
    repairs_complete = models.BooleanField(null=True, blank=True)
    repairs_complete_timestamp = models.DateTimeField(null=True, blank=True)
    mechanic = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="repair_mechanic", null=True, blank=True
    )
    supervised_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="repair_supervised_by",
        null=True,
        blank=True,
    )
    type = models.CharField(max_length=255, choices=type_choices, null=True, blank=True)
    humanUuid = models.CharField(max_length=150, null=True, blank=True)
    perform_fix = models.BooleanField(null=True, blank=True)
    assessment_verified = models.BooleanField(null=True, blank=True)
    assessment_verification_timestamp = models.DateTimeField(null=True, blank=True)
    requisition_required = models.BooleanField(null=True, blank=True)
    repairs_started = models.BooleanField(null=True, blank=True)
    repairs_verified = models.BooleanField(null=True, blank=True)
