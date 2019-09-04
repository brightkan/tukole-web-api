from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from model_utils.models import TimeStampedModel

from api.models import Site, User
from api.tasks import send_challenge_email


class Challenge(TimeStampedModel):
    challenge_type = (('external', 'External'), ('internal', 'Internal'))
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=challenge_type)
    site = models.ForeignKey(
        to=Site, related_name="challenge_site", on_delete=models.CASCADE, null=True, blank=True
    )
    user = models.ForeignKey(
        to=User, related_name="challenge_user", on_delete=models.CASCADE, null=True, blank=True
    )
    image = models.FileField(upload_to='challenge', null=True, blank=True)
    description = models.TextField()


@receiver(post_save, sender=Challenge)
def send_new_challenge_email(sender, instance, created, **kwargs):
    if created:
        project_managers = User.objects.filter(role__contains='project_manager')
        for pm in project_managers:
            send_challenge_email.delay(pm.id, instance.user.id, instance.id)
