	
# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.surveys import Survey
from api.serializers.surveys import SurveySerializer


# Create your views here.

class SurveyViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('creator','surveyor','ack_user')

