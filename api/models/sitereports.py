from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User
from api.models.workspaces import Workspace
from api.models.sites import Site


# Create your models here.


class Sitereport(TimeStampedModel):
    site = models.ForeignKey(
        Site, on_delete=models.CASCADE, null=True, blank=True, related_name="sitereports_site"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="sitereports_user"
    )
    report = models.CharField(max_length=500, null=True)
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="sitereports_workspace",
    )
