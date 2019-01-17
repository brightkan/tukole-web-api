# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from api.models import Company
from api.serializers.company import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
