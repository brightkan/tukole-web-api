from django.utils.six import text_type
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, PasswordField
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import Workspace
from api.models.users import UserWorkSpace


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super(MyTokenObtainPairSerializer, self).__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField()
        self.fields['workspace'] = serializers.CharField()

    def validate(self, attrs):
        workspace_ = attrs['workspace']
        data = super(TokenObtainPairSerializer, self).validate(attrs)

        refresh = self.get_token(self.user)
        workspace = Workspace.objects.filter(name__icontains=workspace_).first()
        part_of_workspace = False
        if workspace:
            if UserWorkSpace.objects.filter(workspace=workspace, user=self.user).first():
                part_of_workspace = True
                data['refresh'] = text_type(refresh)
                data['access'] = text_type(refresh.access_token)
                data['user_id'] = self.user.id
                data['user_type'] = self.user.type
                data['workspace'] = workspace.id
        data['part_of_workspace'] = part_of_workspace

        return data


class TukoleObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
