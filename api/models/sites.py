from django.db import models
from model_utils.models import TimeStampedModel

from api.models.users import User
from api.models.workspaces import Workspace


# Create your models here.

class Sites(TimeStampedModel):
    site_name = models.CharField(max_length=50, null=True)
    location_lat = models.CharField(max_length=20, null=True)
    location_long = models.CharField(max_length=20, null=True)
    start_date = models.DateField(null=True)
    expected_end_date = models.DateField(null=True)
    clientId = models.ForeignKey(User, on_delete=models.CASCADE)
    ackStatus = models.BooleanField(default=False)
    current_stage = models.IntegerField(default=0)
    archivedStatus = models.BooleanField(default=False)
    workspace_id = models.ForeignKey(Workspace, on_delete=models.CASCADE, null=True,default=1)
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)
