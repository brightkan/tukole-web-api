from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class Tools_types(TimeStampedModel):
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
