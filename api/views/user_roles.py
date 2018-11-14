from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models.user_roles import UserRoles
from api.serializers.user_roles import UserRolesSerializer


class UserRolesViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserRolesSerializer
    queryset = UserRoles.objects.all()
