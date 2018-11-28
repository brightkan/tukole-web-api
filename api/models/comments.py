from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Site, User


class Comment(TimeStampedModel):
    priority_choices = (
        ('high', 'High'),
        ('low', 'Low'),
        ('medium', 'Medium'),
    )
    site = models.ForeignKey(to=Site, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    priority = models.CharField(max_length=255, null=True, blank=True, choices=priority_choices)
    affected_teams = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(to=User, null=True, blank=True, on_delete=models.CASCADE)
