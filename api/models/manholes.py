from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Site, User


class ManHole(TimeStampedModel):
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=150)
    missed = models.BooleanField(default=False)


class ManHoleDuration(TimeStampedModel):
    manhole = models.ForeignKey(to=ManHole, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    from_tube = models.CharField(max_length=150, null=True, blank=True)
    from_fibers = models.CharField(max_length=150, null=True, blank=True)
    to_tube = models.CharField(max_length=150, null=True, blank=True)
    to_fibers = models.CharField(max_length=150, null=True, blank=True)


class ManHoleAssignment(TimeStampedModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    manhole = models.ForeignKey(to=ManHole, on_delete=models.CASCADE)
    fm_approved = models.BooleanField(null=True, blank=True)


class ManHoleInstallation(TimeStampedModel):
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    number_installed = models.IntegerField(null=True, blank=True)
    fm_approved = models.BooleanField(null=True, blank=True)


class HandHoleInstallation(TimeStampedModel):
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    number_installed = models.IntegerField(null=True, blank=True)
    fm_approved = models.BooleanField(null=True, blank=True)


class ODFInstallation(TimeStampedModel):
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    number_of_odf_installed = models.IntegerField(null=True, blank=True)
    size_of_odf = models.CharField(max_length=255, null=True, blank=True)


class ODFTermination(TimeStampedModel):
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    ports = models.IntegerField(null=True, blank=True)
    client = models.CharField(max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)


class DuctInstallation(TimeStampedModel):
    duct_type_choices = (
        ('HDPE', 'HDPE'),
        ('PVC', 'PVC'),
    )
    micro_duct_choices = (
        ('1_way', '1 Way'),
        ('2_way', '2 Way'),
        ('3_way', '3 Way'),
    )
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    duct_type = models.CharField(max_length=155, choices=duct_type_choices, null=True, blank=True)
    micro_duct = models.CharField(max_length=155, choices=micro_duct_choices, null=True, blank=True)
    size = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)


class CableInstallation(TimeStampedModel):
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    method = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    size = models.CharField(max_length=255, null=True, blank=True)
    length = models.CharField(max_length=255, null=True, blank=True)


class Trunking(TimeStampedModel):
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    meters_trunked = models.CharField(max_length=255, null=True, blank=True)
