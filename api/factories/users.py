from factory import Factory
from pytest_factoryboy import register

from api.models import User


@register
class UserFactory(Factory):
    class Meta:
        model = User

    email = 'test@tukole.co.ug'
