from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Site


class ManHole(TimeStampedModel):
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=150)