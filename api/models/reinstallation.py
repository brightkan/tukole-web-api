from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Site, User


class ReInstallation(TimeStampedModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE)
    amount = models.IntegerField()
    type = models.CharField(max_length=255)
    fm_approved = models.BooleanField(null=True, blank=True)
