from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Site, User


class ManHole(TimeStampedModel):
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=150)


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
