from rest_framework import serializers

from api.models.users import UserWorkSpace


class UserWorkSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWorkSpace
        fields = ('id', 'workspace')
