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


"""
    @action(detail=False, url_path='invite', url_name="invite-members", serializer_class=UserSerializer)
    def invite_members(self, request):

        pass



signer = TimestampSigner()
+    value = signer.sign('LuGeLo510!!')
+    ttl = value.split(":")
+    token = ('%s%s' % (ttl[2], ttl[1]))
+    return token

token = str(request.GET['ttl'])
+        signer = TimestampSigner()
+        first_ = token[-6:]
+        second_ = token[:-6]
+        hash = ("%s:%s:%s" % ("LuGeLo510!!", first_, second_))
+        try:
+            signer.unsign(hash, max_age=timedelta(seconds=60*10))
"""
