from django.db import models

# Create your models here.

class Machinery(models.Model):
    name = models.CharField(max_length=50,null=True)
    uuid = models.CharField(max_length=50,null=True)
    humanUuid = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50,null=True)

