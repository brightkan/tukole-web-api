from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User
from api.models.notifications import Notification
from api.models.workspaces import Workspace


# Create your models here.

class Site(TimeStampedModel):
    site_name = models.CharField(max_length=50, null=True)
    site_deleted = models.BooleanField(default=False, null=True)
    site_accessible = models.BooleanField(default=False, null=True)
    site_surveyed = models.BooleanField(default=False, null=True)
    location_lat = models.CharField(max_length=20, null=True)
    location_long = models.CharField(max_length=20, null=True)
    start_date = models.DateField(null=True)
    survey_date = models.DateField(null=True)
    expected_end_date = models.DateField(null=True)
    clientId = models.ForeignKey(User, on_delete=models.CASCADE)
    current_stage = models.IntegerField(default=0)
    archivedStatus = models.BooleanField(default=False)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, null=True, blank=True,
                                  related_name="sites_workspace")
    surveyor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="site_surveyor")
    ackStatus = models.BooleanField(default=False)
    ack_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="site_ack_user")
    ack_date = models.DateField(null=True)

    def save(self, *args, **kwargs):
        clientId = self.clientId
        ackStatus = self.ackStatus
        print(ackStatus)
        note = 'Survey request was acknowledged'
        super(Site, self).save(*args, **kwargs)

        if ackStatus == True:
            print(note)
            p = Notification(user=clientId, notification=note)
            p.save()
