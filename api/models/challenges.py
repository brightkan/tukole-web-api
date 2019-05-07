from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Site, User


class Challenge(TimeStampedModel):
    challenge_type = (
        ('external', 'External'),
        ('internal', 'Internal')
    )
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=challenge_type)
    site = models.ForeignKey(to=Site, related_name="challenge_site", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(to=User, related_name="challenge_user", on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(upload_to='challenge', null=True, blank=True)
    description = models.TextField()
