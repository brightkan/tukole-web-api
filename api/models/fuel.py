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
    type_choices = (
        ('machine', 'Machine'),
        ('fleet', 'Fleet')
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    fleet = models.ForeignKey(to=Fleet, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=155, choices=type_choices, null=True, blank=True)
    requested_fuel_in_litres = models.IntegerField(null=True, blank=True)
    received_fuel_in_litres = models.IntegerField(null=True, blank=True)
    allow_full_tank = models.BooleanField(default=False)
    pump_screenshot = models.FileField(upload_to='fuel/screenshot', null=True, blank=True)
    fuel_amount = models.IntegerField(null=True, blank=True)
    mileage_at_fuelling_time = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(choices=fuel_status)
    approved = models.BooleanField(default=False)
    refuel_reject_reason = models.CharField(null=True, blank=True, max_length=250)


class FuelReceipt(TimeStampedModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    fleet = models.ForeignKey(to=Fleet, on_delete=models.CASCADE)
    fuel_in_litres = models.IntegerField(null=True, blank=True)
    total_fuel = models.IntegerField(null=True, blank=True)
