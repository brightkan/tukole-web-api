# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.challenges import Challenge
from api.serializers.challenges import ChallengeSerializer


# Create your views here.

class ChallengeViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site', 'user')
