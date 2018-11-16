from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class UserRoles(TimeStampedModel):
    isp = models.CharField(max_length=50, null=True)
    osp = models.CharField(max_length=50, null=True)
    quality = models.CharField(max_length=50, null=True)
    ofc = models.CharField(max_length=50, null=True)
    driver = models.CharField(max_length=50, null=True)
    surveyor = models.CharField(max_length=50, null=True)
    project_manager = models.CharField(max_length=50, null=True)
    fleet_manager = models.CharField(max_length=50, null=True)
