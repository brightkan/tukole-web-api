from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel
from api.models.workspaces import Workspace


class FleetType(TimeStampedModel):
    type = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=150, null=True)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, null=True, blank=True, related_name="fleettype_workspace")

