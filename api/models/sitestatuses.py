from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User
from api.models.sites import Site


# Create your models here.


class Sitestatus(TimeStampedModel):
    site = models.ForeignKey(
        Site, on_delete=models.CASCADE, null=True, blank=True, related_name="sitestatus_site"
    )
    current_status = models.BooleanField(default=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="sitestatus_user"
    )
