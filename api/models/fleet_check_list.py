from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Fleet, User, Workspace


class FleetCheckListItem(TimeStampedModel):
    name = models.CharField(max_length=255, null=True)
    workspace = models.ForeignKey(to=Workspace, null=True, on_delete=models.CASCADE)


class FleetCheckList(TimeStampedModel):
    status_choices = (
        ('ok', 'Ok'),
        ('not-ok', 'Not ok')
    )
    fleet = models.ForeignKey(to=Fleet, null=True, on_delete=models.CASCADE)
    workspace = models.ForeignKey(to=Workspace, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, null=True, on_delete=models.CASCADE)
    fleet_check_list_item = models.ForeignKey(to=FleetCheckListItem, null=True, on_delete=models.CASCADE)
    status = models.CharField(null=True, choices=status_choices, max_length=150)
