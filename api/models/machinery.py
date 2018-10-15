from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class Machinery(TimeStampedModel):
    name = models.CharField(max_length=50,null=True)
    uuid = models.CharField(max_length=50,null=True)
    humanUuid = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50,null=True)

