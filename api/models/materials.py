from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Workspace


class Material(TimeStampedModel):
    name = models.CharField(max_length=255)
    workspace = models.ForeignKey(to=Workspace, on_delete=models.CASCADE, null=True, blank=True,
                                  related_name="material_workspace")

