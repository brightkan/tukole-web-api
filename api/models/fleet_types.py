from django.db import models



# Create your models here.

class Fleet_types(models.Model):
    type = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=150,null=True)
    
