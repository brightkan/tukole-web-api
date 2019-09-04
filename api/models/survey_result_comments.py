from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel

from api.models import User
from api.models.notifications import Notification
from api.models.survey_results import SurveyResult


class SurveyResultComment(TimeStampedModel):
    survey_result = models.ForeignKey(
        SurveyResult,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="SurveyResult_survey_result",
    )
    comment = models.CharField(max_length=255)
    readStatus = models.BooleanField(default=False)
    surveyor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="surveyresultscoments_surveyor",
    )

    def save(self, *args, **kwargs):
        surveyor = self.surveyor
        note = 'There is a new comment on the uploaded survey resutls'
        print("There is a new comment on the uploaded survey resutls")
        p = Notification(user=surveyor, notification=note)
        p.save()
        super(SurveyResultComment, self).save(*args, **kwargs)
