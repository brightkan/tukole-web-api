from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class Material(TimeStampedModel):
    name = models.CharField(max_length=50, null=True)
    measurement = models.CharField(max_length=150, null=True)
    unit_cost= models.CharField(max_length=50, null=True)
