from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User
from api.models.sites import Site
from api.models.tools import Tool


# Create your models here.

class Sitetool(TimeStampedModel):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, null=True, blank=True, related_name="sitetools_tool")
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True, blank=True, related_name="sitetools_site")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="sitetools_user")
