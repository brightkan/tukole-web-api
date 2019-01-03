from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from api.models import Workspace


class MyUserManager(BaseUserManager):
    def create_user(self, password, **extra_fields):
        if not id:
            raise ValueError('The Id must be set')
        # email = self.normalize_email(email)
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, id, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(password, **extra_fields)


class AbstractEmailUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(null=True)
    workspace = models.ForeignKey(to=Workspace, null=True, on_delete=models.CASCADE)
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
    USERNAME_FIELD = 'id'
    objects = MyUserManager()

    def __str__(self):
        return str(self.email)

    def get_full_name(self):
        return str(self.email)

    def get_short_name(self):
        return str(self.email)

    class Meta:
        unique_together = ('email', 'workspace',)


class User(AbstractEmailUser, TimeStampedModel):
    user_types = (
        ('admin', 'Admin'),
        ('super_admin', 'Super Admin'),
        ('employee', 'Employee'),
        ('client', 'Client'),
    )

    contract_type_choices = (
        ('permanent', 'permanent'),
        ('temporary', 'temporary'),

    )
    role_choices = (
        ('isp', 'ISP'),
        ('osp', 'OSP'),
        ('quality', 'Quality'),
        ('ofc', 'OFC'),
        ('driver', 'Driver'),
        ('surveyor', 'Surveyor'),
        ('project_manager', 'Project Manager'),
        ('fleet_manager', 'Fleet Manager'),
        ('mechanic', 'Mechanic'),

    )
    type = models.CharField(max_length=150, choices=user_types)
    role = models.CharField(max_length=150, choices=role_choices, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    contract_type = models.CharField(max_length=150, choices=contract_type_choices)
    phone_number = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return "%s %s %s" % (self.id, self.first_name, self.last_name)


class UserEmailActivation(TimeStampedModel):
    email = models.EmailField()
    token = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.email


class UserWorkSpace(TimeStampedModel):
    user = models.ForeignKey(to=User, related_name="user_workspace_user", on_delete=models.CASCADE, db_index=True)
    workspace = models.ForeignKey(to=Workspace, related_name="user_workspace_workspace", on_delete=models.CASCADE,
                                  db_index=True)

    class Meta:
        unique_together = ('user', 'workspace',)

    def __str__(self):
        return "%s %s" % (self.user, self.workspace)
