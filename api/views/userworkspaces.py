from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from api.models.users import UserWorkSpace
from api.serializers.userworkspaces import UserWorkSpaceSerializer


class UserWorkSpaceViewSet(ModelViewSet):
    """
    Users API
    ---
        :
    request_serializer: UserSerializer
    response_serializer: UserSerializer
    """

    serializer_class = UserWorkSpaceSerializer
    model = UserWorkSpace
    queryset = UserWorkSpace.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user',)
