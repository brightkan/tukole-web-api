from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Site, User


class Incident(TimeStampedModel):
    incident_type = (
        ('external', 'External'),
        ('internal', 'Internal')
    )
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=incident_type)
    site = models.ForeignKey(to=Site, related_name="incident_site", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(to=User, related_name="incident_user", on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(upload_to='challenge', null=True, blank=True)
    description = models.TextField()
