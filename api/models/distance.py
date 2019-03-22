from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Site, User


class TrenchedDistance(TimeStampedModel):
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    distance = models.IntegerField()
    depth = models.IntegerField()
    fm_approved = models.BooleanField(null=True, blank=True)
