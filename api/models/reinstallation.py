from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Material, Site, User


class ReInstallation(TimeStampedModel):
    material = models.ForeignKey(to=Material, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE)
    amount = models.IntegerField()
    type = models.CharField(max_length=255)
