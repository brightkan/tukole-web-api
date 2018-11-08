from django.db import models
# Create your models here.
from model_utils.models import TimeStampedModel

from api.models.survey_results import SurveyResult


class SurveyResultComment(TimeStampedModel):
    survey_result= models.ForeignKey(SurveyResult, on_delete=models.CASCADE, null=True, blank=True, related_name="SurveyResult_survey_result")
    comment= models.CharField(max_length=255)
    readStatus=models.BooleanField(default=False)
