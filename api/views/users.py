from datetime import timedelta

from django.core.signing import TimestampSigner
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from api.models import User
from api.models.users import UserEmailActivation, UserWorkSpace
from api.serializers.users import UserSerializer, SimpleInviteUserSerializer, AcceptUserSerializer
from api.tasks import send_invite_email


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

    @action(methods=['post'], detail=False, url_path='invite', url_name="invite-members",
            serializer_class=SimpleInviteUserSerializer)
    def invite_members(self, request):
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        workspace = request.data['workspace']
        type = request.data['type']
        user, created = User.objects.get_or_create(email=email,
                                                   defaults={'first_name': first_name, 'last_name': last_name,
                                                             'type': type})

        signer = TimestampSigner()
        value = signer.sign(email)
        print("oktkenalksdkashdklahslkdas dalksdhaklh token")
        print(value)
        ttl = value.split(":")
        token = ('%s%s' % (ttl[1], ttl[2]))
        email_activation_, created = UserEmailActivation.objects.get_or_create(email=email, defaults={'token': token})
        user_workspace, created = UserWorkSpace.objects.get_or_create(
            workspace_id=workspace,
            user_id=user.id
        )
        send_invite_email.delay(user.id, token, self.request.user.id)
        user_data = UserSerializer(user).data
        return Response(data=user_data, status=HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='accept', url_name="accept-members",
            serializer_class=AcceptUserSerializer)
    def accept_users(self, request):
        token = request.data['token']
        password = request.data['password']
        email_activation_token = UserEmailActivation.objects.filter(token=token).first()
        token_first_part = token[:6]
        token_second_part = token[6:]

        signer = TimestampSigner()
        email_hash = ("%s:%s:%s" % (email_activation_token.email, token_first_part, token_second_part))
        print("as;dlja;ldjlasjd;ljas;d")
        print(email_hash)
        try:
            unsigned_value = signer.unsign(email_hash, max_age=timedelta(days=3))
            if unsigned_value == email_activation_token.email:
                user = User.objects.filter(email=email_activation_token.email).first()
                user.set_password(password)
                user.save()
                email_activation_token.is_verified = True
                email_activation_token.save()
                data = {'status': True, 'message': "User password sent successfully"}
                return Response(data=data, status=HTTP_200_OK)

        except Exception as e:
            print(e)
            data = {'status': False,
                    'message': "User invite expired. Please have the admin reinvite you to the workspace"}
            return Response(data=data, status=HTTP_200_OK)
