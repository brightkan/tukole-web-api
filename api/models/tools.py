from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Workspace, ToolType


# Create your models here.

class Tool(TimeStampedModel):
    name = models.CharField(max_length=50, null=True)
    type = models.ForeignKey(ToolType, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=50, null=True)
    humanUuid = models.CharField(max_length=50, null=True)
    workspace = models.ForeignKey(to=Workspace, on_delete=models.CASCADE, null=True, blank=True,
                                  related_name="tools_workspace")
