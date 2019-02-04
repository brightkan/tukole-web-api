from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Fleet, User


class Fuel(TimeStampedModel):
    fleet = models.ForeignKey(to=Fleet, on_delete=models.CASCADE)
    cost = models.IntegerField()
    litres = models.IntegerField()
    mileage = models.IntegerField()
    fueled_by = models.ForeignKey(User, on_delete=models.CASCADE)


class FleetFuelRequest(TimeStampedModel):
    fuel_status = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    fleet = models.ForeignKey(to=Fleet, on_delete=models.CASCADE)
    requested_fuel_in_litres = models.IntegerField(null=True, blank=True)
    received_fuel_in_litres = models.IntegerField(null=True, blank=True)
    total_fuel_amount = models.IntegerField(null=True, blank=True)
    mileage_at_fuelling_time = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(choices=fuel_status)
    refuel_reject_reason = models.CharField(null=True, blank=True, max_length=250)
