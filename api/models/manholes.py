from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Site, User


class ManHole(TimeStampedModel):
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=150)


class ManHoleDuration(TimeStampedModel):
    manhole = models.ForeignKey(to=ManHole, on_delete=models.CASCADE)
    duration = models.IntegerField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)


class ManHoleAssignment(TimeStampedModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    manhole = models.ForeignKey(to=ManHole, on_delete=models.CASCADE)
