from django.db import models
from model_utils.models import TimeStampedModel

from api.models.materials import Material
from api.models.sites import Site


# Create your models here.


class WarehouseMaterial(TimeStampedModel):
    site = models.ForeignKey(
        Site, on_delete=models.CASCADE, null=True, blank=True, related_name="warehousematerial_site"
    )
    is_returned = models.BooleanField(default=False)
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="warehousematerial_material",
    )
    quantity = models.IntegerField(default=0)
