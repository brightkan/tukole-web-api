from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class Workspace(TimeStampedModel):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
