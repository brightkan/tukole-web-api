from django.contrib.auth import authenticate
from django.utils.six import text_type
from rest_framework import serializers
from rest_framework_simplejwt.serializers import PasswordField
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import Workspace
from api.models.users import UserWorkSpace, User


class MyTokenObtainPairSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super(MyTokenObtainPairSerializer, self).__init__(*args, **kwargs)

        self.fields['email'] = serializers.EmailField()
        self.fields['password'] = PasswordField()
        self.fields['workspace'] = serializers.CharField()

    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        print(attrs)
        workspace_ = attrs['workspace']
        email_ = attrs['email']
        password_ = attrs['password']
        data = {}
        authed_user = None
        workspace = Workspace.objects.filter(name__icontains=workspace_).first()

        user_ = User.objects.filter(email=email_).exists()
        user_instances = User.objects.filter(email=email_)
        user_ids = User.objects.filter(email=email_).values_list('id', flat=True)
        user_ids = list(user_ids)

        authed_user_ids = []
        for user_id in user_ids:
            authed_user = authenticate(**{'id': user_id, 'password': password_})
            if authed_user:
                authed_user_ids.append(user_id)

        if not authed_user_ids:
            raise serializers.ValidationError('No active account found with the given credentials')

        if not workspace:
            raise serializers.ValidationError('No workspace with that name found in the system')

        user_workspace = UserWorkSpace.objects.filter(workspace=workspace, user_id__in=authed_user_ids)

        if not user_workspace:
            raise serializers.ValidationError('User is not part of that workspace')

        else:
            authed_user = authenticate(**{'id': user_workspace[0].user.id, 'password': password_})
            refresh = self.get_token(authed_user)
            part_of_workspace = True
            data['refresh'] = text_type(refresh)
            data['access'] = text_type(refresh.access_token)
            data['user_id'] = authed_user.id
            data['user_role'] = authed_user.role
            data['user_type'] = authed_user.type
            data['workspace'] = workspace.id
            data['company'] = authed_user.company.id if authed_user.company else ""
            data['part_of_workspace'] = part_of_workspace
            return data


class TukoleObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
