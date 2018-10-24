from copy import deepcopy

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import User
from api.models.users import UserWorkSpace


class UserSerializer(ModelSerializer):
    workspace = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    user_workspace = serializers.SerializerMethodField(read_only=True)

    def get_user_workspace(self, obj):
        workspace = UserWorkSpace.objects.filter(user=obj).values_list('workspace', flat=True)
        return workspace[0]

    def create(self, validated_data):
        all_data = deepcopy(validated_data)
        print(all_data)
        workspace = all_data.pop('workspace')
        print(workspace)
        user = User.objects.create_user(**all_data)
        user_workspace, created = UserWorkSpace.objects.get_or_create(
            workspace_id=workspace,
            user=user
        )
        return user

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'type', 'contract_type',
                  'phone_number', 'workspace', 'password', 'user_workspace')
