from django.db import models
from model_utils.models import TimeStampedModel

from api.models.tools_types import Tools_types
from api.models.workspaces import Workspace


# Create your models here.

class Tools(TimeStampedModel):
    name = models.CharField(max_length=50, null=True)
    type = models.ForeignKey(Tools_types, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=50, null=True)
    humanUuid = models.CharField(max_length=50, null=True)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, null=True, blank=True,
                                  related_name="tools_workspace")
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)
