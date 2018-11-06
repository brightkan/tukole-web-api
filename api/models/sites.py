from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User
from api.models.workspaces import Workspace
from api.models.surveys import Survey

# Create your models here.

class Site(TimeStampedModel):
    site_name = models.CharField(max_length=50, null=True)
    location_lat = models.CharField(max_length=20, null=True)
    location_long = models.CharField(max_length=20, null=True)
    start_date = models.DateField(null=True)
    survey_request= models.ForeignKey(Survey, on_delete=models.CASCADE, null=True, blank=True,related_name="sites_survey_request")
    survey_date = models.DateField(null=True)
    expected_end_date = models.DateField(null=True)
    clientId = models.ForeignKey(User, on_delete=models.CASCADE)
    ackStatus = models.BooleanField(default=False)
    current_stage = models.IntegerField(default=0)
    archivedStatus = models.BooleanField(default=False)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, null=True, blank=True,related_name="sites_workspace")
                                  