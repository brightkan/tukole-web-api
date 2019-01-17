from django.db import models
from model_utils.models import TimeStampedModel


class Company(TimeStampedModel):
    name = models.CharField(max_length=255)
