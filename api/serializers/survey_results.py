from rest_framework import serializers

from api.models.survey_results import SurveyResult


class SurveyResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResult
        fields = ('id', 'file_url', 'title', 'site', 'surveyor', 'acceptStatus', 'number_of_comments', 'created')
