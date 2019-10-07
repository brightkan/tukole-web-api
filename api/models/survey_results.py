from django.db import models
from model_utils.models import TimeStampedModel

# from api.models import Workspace, MachineryType
from api.models import User
from api.models.notifications import Notification
from api.models.sites import Site


# Create your models here.


class SurveyResult(TimeStampedModel):
    file_url = models.FileField(upload_to='files', null=True)
    title = models.CharField(max_length=50, null=True)
    site = models.ForeignKey(
        Site, on_delete=models.CASCADE, null=True, blank=True, related_name="surveyresult_site"
    )
    surveyor = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="surveyresult_surveyor"
    )
    acceptStatus = models.BooleanField(default=False)
    description = models.TextField(default=False)

    def number_of_comments(self):
        from api.models.survey_result_comments import SurveyResultComment

        return SurveyResultComment.objects.filter(survey_result=self).count()

    def save(self, *args, **kwargs):
        surveyor = self.surveyor
        acceptStatus = self.acceptStatus
        note1 = 'Pending Review'
        note2 = 'survey_results_accepted'
        note3 = 'Survey results were rejected'

        if acceptStatus is None:
            print("Pending Review")
            p = Notification(user=surveyor, notification=note1)
            p.save()
            super(SurveyResult, self).save(*args, **kwargs)

        elif acceptStatus:  # shouldn't do this
            print("survey_results_accepted")
            p = Notification(user=surveyor, notification=note2)
            p.save()
            super(SurveyResult, self).save(*args, **kwargs)

        else:
            print("Survey results were rejected")
            p = Notification(user=surveyor, notification=note3)
            p.save()
            super(SurveyResult, self).save(*args, **kwargs)
