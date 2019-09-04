from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models.survey_results import SurveyResult
from api.serializers.survey_results import SurveyResultSerializer


class SurveyResultViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SurveyResultSerializer
    queryset = SurveyResult.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site', 'surveyor')
