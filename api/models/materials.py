from django.db import models
# Create your models here.
from model_utils.models import TimeStampedModel

from api.models import Workspace, Site


class Material(TimeStampedModel):
    name = models.CharField(max_length=255)
    workspace = models.ForeignKey(to=Workspace, on_delete=models.CASCADE, null=True, blank=True,
                                  related_name="material_workspace")
    measurement = models.CharField(max_length=150, null=True)
    unit_cost = models.CharField(max_length=50, null=True)
    running_out = models.BooleanField(default=False)
    quantity = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)


class UsedMaterial(TimeStampedModel):
    object_id = models.CharField(max_length=255, null=True, blank=True)
    object_type = models.CharField(max_length=255, null=True, blank=True)
    material = models.ForeignKey(to=Material, on_delete=models.CASCADE, null=True, blank=True, )
    quantity = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
