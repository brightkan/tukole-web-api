from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from api.models import Workspace


class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class AbstractEmailUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return str(self.email)

    def get_full_name(self):
        return str(self.email)

    def get_short_name(self):
        return str(self.email)


class User(AbstractEmailUser, TimeStampedModel):
    user_types = (
        ('admin', 'Admin'),
        ('super_admin', 'Super Admin'),
        ('employee', 'Employee'),
    )

    contract_type_choices = (
        ('permanent', 'permanent'),
        ('temporary', 'temporary'),

    )
    type = models.CharField(max_length=150, choices=user_types)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    contract_type = models.CharField(max_length=150, choices=contract_type_choices)
    phone_number = models.CharField(max_length=150)
    workspace = models.ForeignKey(to=Workspace, related_name="user_workspace", null=True, blank=True,
                                  on_delete=models.SET_NULL)

    def __str__(self):
        return "%s %s %s" % (self.id, self.first_name, self.last_name)
