from django.db import models
from api.models.users import User

# Create your models here.
 
class Sites (models.Model):
    site_name = models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=50,null=True)
    clientId = models.ForeignKey(User, on_delete=models.CASCADE)
    ackStatus = models.BooleanField(default=False)
    workStatus = models.CharField(max_length=50,null=True)
    archivedStatus = models.CharField(max_length=50,null=True)
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)
    
	

