from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


#from api.models import Workspace, MachineryType
from api.models.workspaces import Workspace
from api.models.machinery_types import MachineryType


class Machinery(TimeStampedModel):
    name = models.CharField(max_length=50, null=True)
    type = models.ForeignKey(MachineryType, on_delete=models.CASCADE, null=True, blank=True,related_name="machinery_types")
    uuid = models.CharField(max_length=50, null=True)
    humanUuid = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, null=True, blank=True, related_name="machinery_workspace")

