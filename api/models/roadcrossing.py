from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Site, User, Machinery
from api.models.tools import Tool


class RoadCrossing(TimeStampedModel):
    distance_crossed = models.IntegerField()
    tool = models.ForeignKey(to=Tool, on_delete=models.CASCADE, null=True, blank=True)
    machinery = models.ForeignKey(to=Machinery, on_delete=models.CASCADE, null=True, blank=True)
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    fm_approved = models.BooleanField(null=True, blank=True)
