from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel

from api.models import Workspace


class Machinery(TimeStampedModel):
    name = models.CharField(max_length=50, null=True)
    uuid = models.CharField(max_length=50, null=True)
    humanUuid = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
    workspace = models.ForeignKey(to=Workspace, on_delete=models.CASCADE, null=True, blank=True,
                                  related_name="machinery_workspace")

