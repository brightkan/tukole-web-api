from django.contrib import admin

# Register your models here.
from api.models import User, Fleet, Machinery, ToolType, Site, Workspace
from api.models.fleet_types import FleetType
from api.models.tools import Tool
from api.models.users import UserEmailActivation, UserWorkSpace

admin.site.register(User)
admin.site.register(Tool)
admin.site.register(Fleet)
admin.site.register(FleetType)
admin.site.register(Machinery)
admin.site.register(Site)
admin.site.register(ToolType)
admin.site.register(UserEmailActivation)
admin.site.register(Workspace)
admin.site.register(UserWorkSpace)
