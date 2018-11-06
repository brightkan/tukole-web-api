from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User
from api.models.workspaces import Workspace


# Create your models here.

class Survey(TimeStampedModel):
    creator= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="survey_creator")
    site_name= models.CharField(max_length=50, null=True)
    coordinates_lat= models.CharField(max_length=20, null=True)
    coordinates_long= models.CharField(max_length=20, null=True)
    surveyor= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="survey_surveyor")
    ack=models.BooleanField(default=False)
    ack_user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="survey_ack_user")