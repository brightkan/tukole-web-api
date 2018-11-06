from django.db import models
#Create your models here.

from model_utils.models import TimeStampedModel
#from api.models import Workspace, MachineryType
from api.models import User

class Notification(TimeStampedModel):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="notification_user")
    notification=models.CharField(max_length=500, null=True)
    read=models.BooleanField(default=False)


