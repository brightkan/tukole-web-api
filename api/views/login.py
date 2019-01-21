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

        user_ = User.objects.filter(email=email_).first()
        if user_:
            authed_user = authenticate(**{
                'id': user_.id,
                'password': password_,
            })
            print("##################################################")
            print(authed_user)

        if authed_user is None:
            raise serializers.ValidationError(
                'No active account found with the given credentials',
            )

        else:
            refresh = self.get_token(authed_user)
            workspace = Workspace.objects.filter(name__icontains=workspace_).first()
            print(workspace)
            part_of_workspace = False
            if workspace:
                if UserWorkSpace.objects.filter(workspace=workspace, user=authed_user).first():
                    part_of_workspace = True
                    data['refresh'] = text_type(refresh)
                    data['access'] = text_type(refresh.access_token)
                    data['user_id'] = authed_user.id
                    data['user_role'] = authed_user.role
                    data['user_type'] = authed_user.type
                    data['workspace'] = workspace.id
                    data['company'] = authed_user.company
            data['part_of_workspace'] = part_of_workspace

            return data


class TukoleObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
