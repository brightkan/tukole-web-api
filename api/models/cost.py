from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User, Site


class Cost(TimeStampedModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.IntegerField()
