from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from api.models import User
from api.serializers.users import UserSerializer


class UserViewSet(ModelViewSet):
    """
    Users API
    ---
        :
    request_serializer: UserSerializer
    response_serializer: UserSerializer
    """

    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    model = User
    queryset = User.objects.all()
