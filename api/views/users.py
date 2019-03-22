from datetime import timedelta

from django.core.signing import TimestampSigner
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from api.models import User, Site, Company
from api.models.siteroles import Siterole
from api.models.users import UserEmailActivation, UserWorkSpace
from api.serializers.sites import SiteUserRoleSerializer
from api.serializers.users import UserSerializer, SimpleInviteUserSerializer, AcceptUserSerializer, \
    ResetPasswordSerializer
from api.tasks import send_invite_email, send_reset_password_email


class UserFilter(filters.FilterSet):
    workspace = filters.NumberFilter(method='filter_workspace')

    class Meta:
        model = User
        fields = ['workspace', 'company']

    def filter_workspace(self, queryset, name, value):
        user_ids = UserWorkSpace.objects.filter(workspace=value).values_list('user_id', flat=True)
        users = User.objects.filter(id__in=user_ids)
        return users


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
    filter_class = UserFilter
    filter_backends = (DjangoFilterBackend,)

    @action(methods=['post'], detail=False, url_path='invite', url_name="invite-members",
            serializer_class=SimpleInviteUserSerializer)
    def invite_members(self, request):
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        workspace = request.data['workspace']
        contract_type = request.data['contract_type']
        phone_number = request.data['phone_number']
        type = request.data['type']
        role = request.data['role']
        company = request.data.get('company', None)
        user, created = User.objects.get_or_create(email=email, workspace_id=workspace,
                                                   defaults={'first_name': first_name, 'last_name': last_name,
                                                             'type': type, 'contract_type': contract_type,
                                                             'phone_number': phone_number, 'role': role})

        company_ = Company.objects.filter(id=company).first()
        if company_:
            user.company = company_
            user.save()
        signer = TimestampSigner()
        value = signer.sign(email)
        ttl = value.split(":")
        token = ('%s%s' % (ttl[1], ttl[2]))
        email_activation_, created = UserEmailActivation.objects.get_or_create(email=email, token=token)
        user_workspace, created = UserWorkSpace.objects.get_or_create(
            workspace_id=workspace,
            user_id=user.id
        )
        send_invite_email.delay(user.id, token, self.request.user.id, workspace)
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

    @action(methods=['post'], detail=False, url_path='reset', url_name="reset-password",
            serializer_class=ResetPasswordSerializer)
    def reset_password(self, request):
        email = request.data['email']
        user = User.objects.filter(email=email).first()
        if user:
            signer = TimestampSigner()
            value = signer.sign(email)
            ttl = value.split(":")
            token = ('%s%s' % (ttl[1], ttl[2]))
            deleted = UserEmailActivation.objects.filter(email=email).delete()
            email_activation_, created = UserEmailActivation.objects.get_or_create(email=email, token=token)
            send_reset_password_email.delay(user.id, token, )
            data = {'status': True, 'message': 'Password reset sent'}
            return Response(data=data, status=HTTP_200_OK)
        else:
            data = {'error': "User with that email not found", 'status': False}
            return Response(data=data, status=HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='sites', url_name="sites")
    def users_site(self, request, pk):
        user = User.objects.filter(id=pk).first()
        if user:
            users_sites_id = Siterole.objects.filter(user=user).values_list('site', flat=True)
            sites = Site.objects.filter(id__in=users_sites_id)

            data = SiteUserRoleSerializer(sites, context={'user': user.id}, many=True).data
        else:
            data = {"error": "User is not attached to any site"}
        return Response(data=data, status=HTTP_200_OK)
