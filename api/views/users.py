from django.core.signing import TimestampSigner
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from api.models import User
from api.models.users import UserEmailActivation, UserWorkSpace
from api.serializers.users import UserSerializer, SimpleInviteUserSerializer
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
        user, created = User.objects.get_or_create(email=email,
                                                   defaults={'first_name': first_name, 'last_name': last_name})

        signer = TimestampSigner()
        value = signer.sign(email)
        ttl = value.split(":")
        token = ('%s%s' % (ttl[1], ttl[2]))
        email_activation_, created = UserEmailActivation.objects.get_or_create(email=email, defaults={'token': token})
        user_workspace, created = UserWorkSpace.objects.get_or_create(
            workspace_id=workspace,
            user_id=user.id
        )
        send_invite_email.delay(user.id, token, self.request.user.id)
        return Response(data={"email": email, "invited": True}, status=HTTP_200_OK)


"""
        token = str(request.GET['ttl'])
                 signer = TimestampSigner()
                 first_ = token[-6:]
                 second_ = token[:-6]
                 hash = ("%s:%s:%s" % ("LuGeLo510!!", first_, second_))
         
        try:
                         signer.unsign(hash, max_age=timedelta(seconds=60 * 10))

"""
