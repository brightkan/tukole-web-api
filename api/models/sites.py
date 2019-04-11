from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User, Company
from api.models.notifications import Notification
from api.models.workspaces import Workspace


# Create your models here.

class Site(TimeStampedModel):
    site_name = models.CharField(max_length=50, null=True)
    site_deleted = models.BooleanField(default=False, null=True)
    site_completed = models.BooleanField(default=False, null=True)
    site_accessible = models.BooleanField(default=False, null=True)
    site_surveyed = models.BooleanField(default=False, null=True)
    site_accepted = models.BooleanField(default=False, null=True)
    location_lat = models.CharField(max_length=20, null=True)
    location_long = models.CharField(max_length=20, null=True)
    start_date = models.DateField(null=True)
    survey_date = models.DateField(null=True)
    expected_end_date = models.DateField(null=True)
    clientId = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    current_stage = models.IntegerField(default=0)
    archivedStatus = models.BooleanField(default=False)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, null=True, blank=True,
                                  related_name="sites_workspace")
    surveyor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="site_surveyor")
    ackStatus = models.BooleanField(default=False)
    ack_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="site_ack_user")
    ack_date = models.DateField(null=True)
    survay_time = models.TimeField(null=True)
    can_client_view_survey_reports = models.BooleanField(default=False)
    email_remainder_sent = models.BooleanField(default=False)
    site_contact_person = models.CharField(null=True, blank=True, max_length=150)
    site_contact_phone_number = models.IntegerField(null=True, blank=True)
    site_location = models.CharField(null=True, blank=True, max_length=150)
    site_connected = models.BooleanField(default=False)
    site_ready_for_connection = models.BooleanField(default=False)
    site_connection_request_acknowledged = models.BooleanField(default=False)
    site_connection_date = models.DateTimeField(null=True, blank=True)
    number_of_site_fleet = models.IntegerField(null=True, blank=True)
    number_of_members_on_site = models.IntegerField(null=True, blank=True)
    site_image = models.FileField(upload_to="sites/", null=True, blank=True)
    isp_works_complete = models.BooleanField(default=False, null=True)
    osp_works_complete = models.BooleanField(default=False, null=True)
    ofc_works_complete = models.BooleanField(default=False, null=True)
    site_powering_complete = models.BooleanField(default=False, null=True)
    original_trenching_distance = models.IntegerField(null=True, blank=True)
    current_trenching_distance = models.IntegerField(null=True, blank=True)
    site_drawing = models.FileField(upload_to="drawing/", null=True, blank=True)
    site_address = models.TextField(null=True, blank=True)
    site_usd_rate = models.IntegerField(null=True, blank=True)

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


class SiteImage(TimeStampedModel):
    status_choices = (
        ('before', 'before'),
        ('after', 'after'),
    )
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE)
    image = models.FileField(upload_to="siteimages")
    status = models.CharField(choices=status_choices, max_length=255)


class SiteDocument(TimeStampedModel):
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE)
    file = models.FileField(upload_to="sitedocuments")
    title = models.CharField(max_length=255, null=True, blank=True)


class SitePIP(TimeStampedModel):
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE)
    task = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()


class SitePower(TimeStampedModel):
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    material_used = models.CharField(max_length=255, null=True, blank=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    end_time = models.BooleanField(null=True, blank=True)
