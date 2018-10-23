from django.db import models


# Create your models here.

class Workspace(models.Model):
    workspace_id = models.CharField(max_length=50, null=True)
    workspace_name = models.CharField(max_length=50, null=True)
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)
