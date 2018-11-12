from django.db import models
from model_utils.models import TimeStampedModel

from api.models import User
from api.models.sites import Site 
from api.models.user_roles import UserRoles


# Create your models here.

class Siterole(TimeStampedModel):
    site  = models.ForeignKey(Site, on_delete=models.CASCADE, null=True, blank=True,related_name="siteroles_site")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="siteroles_user")
    userrole = models.ForeignKey(UserRoles, on_delete=models.CASCADE, null=True, blank=True,related_name="siterole_userrole")                            							  
    
    def save(self, *args, **kwargs):
        site = self.site
        user = self.user
        userrole = self.userrole
        
        note='You have bean added to site'+site+'as'+userrole
        print(note)        
        p = Notification(user=user,notification=note)
        p.save()