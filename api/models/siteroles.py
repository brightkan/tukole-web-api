from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User
from api.models.notifications import Notification
from api.models.sites import Site


# Create your models here.


class Siterole(TimeStampedModel):
    role_choices = (
        ('isp', 'ISP'),
        ('osp', 'OSP'),
        ('osp_field_manager', 'OSP Field Manager'),
        ('osp_supervisor', 'OSP Supervisor'),
        ('quality', 'Quality'),
        ('ofc', 'OFC'),
        ('driver', 'Driver'),
        ('surveyor', 'Surveyor'),
        ('project_manager', 'Project Manager'),
        ('fleet_manager', 'Fleet Manager'),
        ('mechanic', 'Mechanic'),
        ('fuel_station_user', 'Fuel Station User'),
        ('warehouse', 'warehouse'),
        ('garage_manager', 'Garage Manager'),
        ('workshop_supervisor', 'Workshop Supervisor'),
    )

    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="siteroles_site")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="siteroles_user")
    role = models.CharField(max_length=150, choices=role_choices)

    def save(self, *args, **kwargs):
        site = self.site
        user = self.user

        note = 'You have bean added to site' + site.site_name
        p = Notification(user=user, notification=note)
        p.save()
        super(Siterole, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
