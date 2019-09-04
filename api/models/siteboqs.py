from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User
from api.models.materials import Material
from api.models.sites import Site


# Create your models here.


class Siteboq(TimeStampedModel):
    site = models.ForeignKey(
        Site, on_delete=models.CASCADE, null=True, blank=True, related_name="siteboq_site"
    )
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, null=True, blank=True, related_name="siteboq_material"
    )
    actual_quantity = models.IntegerField(null=True, blank=True)
    estimate_quantity = models.IntegerField(null=True, blank=True)
    boq_type = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="siteboq_user"
    )
    description = models.CharField(max_length=255, null=True, blank=True)
