from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from model_utils.models import TimeStampedModel

from api.models import Site, User
from api.models.sitefleets import Sitefleet
from api.tasks import send_trip_cancel_email


class Trip(TimeStampedModel):
    start = models.CharField(max_length=255, null=True, blank=True)
    start_long = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    start_lat = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    destination = models.CharField(max_length=255, null=True, blank=True)
    destination_long = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    destination_lat = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    site_fleet = models.ForeignKey(to=Sitefleet, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, null=True, blank=True, on_delete=models.CASCADE)
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
    cancelled = models.BooleanField(null=True, blank=True)
    reason_for_cancellation = models.TextField(null=True, blank=True)


class RouteChange(TimeStampedModel):
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    route_change_reason = models.CharField(max_length=255, null=True, blank=True)


class Other(TimeStampedModel):
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)


@receiver(post_save, sender=Trip)
def send_trip_cancelled_email(sender, instance, created, **kwargs):
    if instance.cancelled:
        project_managers = User.objects.filter(
            Q(role__contains='project_manager') | Q(role__contains='fleet_manager'))
        for pm in project_managers:
            trip = Trip.objects.filter(id=instance.id).first()
            send_trip_cancel_email.delay(pm.id, trip.user.id, trip.id)
