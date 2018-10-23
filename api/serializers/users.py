from rest_framework.serializers import ModelSerializer

from api.models import User


class UserSerializer(ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email',
                  'type', 'contract_type', 'phone_number')
        write_only_fields = ('password',)
