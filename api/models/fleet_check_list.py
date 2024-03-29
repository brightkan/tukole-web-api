from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Fleet, User, Workspace
from api.models.fleets import UserFleetAssignment


class FleetCheckListItem(TimeStampedModel):
    type_choices = (('fleet', 'Fleet'), ('machine', 'Machine'))
    type = models.CharField(max_length=255, null=True, blank=True, choices=type_choices)
    name = models.CharField(max_length=255, null=True)
    workspace = models.ForeignKey(to=Workspace, null=True, on_delete=models.CASCADE)


class FleetCheckList(TimeStampedModel):
    status_choices = (('ok', 'Ok'), ('not-ok', 'Not ok'))
    fleet = models.ForeignKey(to=Fleet, null=True, on_delete=models.CASCADE)
    workspace = models.ForeignKey(to=Workspace, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, null=True, on_delete=models.CASCADE)
    fleet_check_list_item = models.ForeignKey(
        to=FleetCheckListItem, null=True, on_delete=models.CASCADE
    )
    status = models.CharField(null=True, choices=status_choices, max_length=150)


class FleetCheckListItemResult(TimeStampedModel):
    status_choices = (('before', 'Before'), ('after', 'after'))

    fleet_check_list_item = models.ForeignKey(
        to=FleetCheckListItem, null=True, on_delete=models.CASCADE
    )
    request_object_id = models.ForeignKey(
        to=UserFleetAssignment, null=True, on_delete=models.CASCADE
    )
    status = models.CharField(max_length=50, null=True, blank=True, choices=status_choices)
