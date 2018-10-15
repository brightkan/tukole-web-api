from django.db import models
from model_utils.models import TimeStampedModel


class Material(TimeStampedModel):
    name = models.CharField(max_length=255)