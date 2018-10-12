from rest_framework.serializers import ModelSerializer

from api.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email',
                  'type', 'contract_type', 'phone_number')
