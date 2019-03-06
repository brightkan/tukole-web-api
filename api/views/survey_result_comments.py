from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models.survey_result_comments import SurveyResultComment
from api.serializers.survey_result_comments import SurveyResultCommentSerializer


class SurveyResultCommentViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SurveyResultCommentSerializer
    queryset = SurveyResultComment.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('survey_result',)
