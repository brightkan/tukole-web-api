from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class Fleet_types(TimeStampedModel):
    type = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=150, null=True)
