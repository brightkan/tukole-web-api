from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
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
    contract_type = models.CharField(max_length=150, choices=contract_type_choices)
    phone_number = models.CharField(max_length=150)

    def __str__(self):
        return "%s %s %s" % (self.id, self.first_name, self.last_name)
