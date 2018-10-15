from django.db import models
from model_utils.models import TimeStampedModel

from api.models.users import User


# Create your models here.

class Sites(TimeStampedModel):
    site_name = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    clientId = models.ForeignKey(User, on_delete=models.CASCADE)
    ackStatus = models.BooleanField(default=False)
    workStatus = models.CharField(max_length=50, null=True)
    archivedStatus = models.CharField(max_length=50, null=True)
