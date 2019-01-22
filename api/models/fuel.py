from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Fleet, User


class Fuel(TimeStampedModel):
    fleet = models.ForeignKey(to=Fleet, on_delete=models.CASCADE)
    cost = models.IntegerField()
    litres = models.IntegerField()
    mileage = models.IntegerField()
    fueled_by = models.ForeignKey(User, on_delete=models.CASCADE)
