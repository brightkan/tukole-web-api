from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Fleet, User, Machinery, Site
from api.models.tools import Tool


class FleetHistory(TimeStampedModel):
    history_type_choices = (
        ('assignment', 'Assignment'),
        ('broken_down', 'Broken Down'),
        ('fixed', 'Fixed'),
    )
    fleet = models.ForeignKey(to=Fleet, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    history_type = models.CharField(max_length=150, choices=history_type_choices)
    time_to_fix = models.IntegerField(blank=True, null=True)
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)


class MachineHistory(TimeStampedModel):
    history_type_choices = (
        ('assignment', 'Assignment'),
        ('broken_down', 'Broken Down'),
        ('fixed', 'Fixed'),
    )
    machine = models.ForeignKey(to=Machinery, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    history_type = models.CharField(max_length=150, choices=history_type_choices)
    time_to_fix = models.IntegerField(blank=True, null=True)
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)


class ToolHistory(TimeStampedModel):
    history_type_choices = (
        ('assignment', 'Assignment'),
        ('broken_down', 'Broken Down'),
        ('fixed', 'Fixed'),
    )
    tool = models.ForeignKey(to=Tool, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    history_type = models.CharField(max_length=150, choices=history_type_choices)
    time_to_fix = models.IntegerField(blank=True, null=True)
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
