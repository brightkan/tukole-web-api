from django.db import models
from model_utils.models import TimeStampedModel

from api.models.siteroles import Siterole


class SiteArrivalTime(TimeStampedModel):
    site_role = models.ForeignKey(to=Siterole, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField()


class SiteWorkStatus(TimeStampedModel):
    work_status_choices = (
        ('started', 'started'),
        ('stopped', 'stopped'),
        ('resumed', 'resumed'),
    )
    site_role = models.ForeignKey(to=Siterole, on_delete=models.CASCADE)
    work_status = models.CharField(choices=work_status_choices, max_length=150)
    reason = models.CharField(null=True, blank=True, max_length=150)


class SiteCompletedWorks(TimeStampedModel):
    site_role = models.ForeignKey(to=Siterole, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
