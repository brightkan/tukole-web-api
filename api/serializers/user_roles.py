	
from rest_framework import serializers

from api.models.user_roles import UserRoles


class UserRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoles
        fields = ('id','isp','osp','quality','ofc','driver','surveyor','project_manager','fleet_manager')


