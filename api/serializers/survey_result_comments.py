from rest_framework import serializers

from api.models.survey_result_comments import SurveyResultComment


class SurveyResultCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResultComment
        fields = ('id', 'survey_result', 'comment', 'readStatus', 'created')
