from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Workspace


class Company(TimeStampedModel):
    name = models.CharField(max_length=255)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, null=True, blank=True)
