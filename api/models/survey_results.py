from django.db import models
#Create your models here.

from model_utils.models import TimeStampedModel
#from api.models import Workspace, MachineryType
from api.models import User
from api.models.sites import Site


class SurveyResult(TimeStampedModel):	
    file_url= models.FileField(upload_to='files', null=True)
    title=models.CharField(max_length=50, null=True)
    site= models.ForeignKey(Site, on_delete=models.CASCADE, null=True, blank=True, related_name="surveyresult_site")
    surveyor= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="surveyresult_surveyor")
    acceptStatus=models.BooleanField(default=False)


