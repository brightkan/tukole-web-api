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
        ('quality', 'Quality'),
        ('ofc', 'OFC'),
        ('driver', 'Driver'),
        ('surveyor', 'Surveyor'),
        ('project_manager', 'Project Manager'),
        ('fleet_manager', 'Fleet Manager'),

    )

    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True, blank=True, related_name="siteroles_site")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="siteroles_user")
    role = models.CharField(max_length=150, choices=role_choices, null=True, blank=True)

    def save(self, *args, **kwargs):
        site = self.site
        user = self.user
        role = self.role

        note = 'You have bean added to site' + site.site_name
        p = Notification(user=user, notification=note)
        p.save()
        super(Siterole, self).save(*args, **kwargs)
