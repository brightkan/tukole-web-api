from django.contrib import admin

# Register your models here.
from api.models import User, Fleet, Machinery, ToolType, Site
from api.models.fleet_types import FleetType
from api.models.tools import Tool
from api.models.users import UserEmailActivation

admin.site.register(User)
admin.site.register(Tool)
admin.site.register(Fleet)
admin.site.register(FleetType)
admin.site.register(Machinery)
admin.site.register(Site)
admin.site.register(ToolType)
admin.site.register(UserEmailActivation)
