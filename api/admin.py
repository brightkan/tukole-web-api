from django.contrib import admin

# Register your models here.
from api.models import User, Fleet, Machinery, Sites
from api.models.fleet_types import Fleet_types
from api.models.tools import Tools
from api.models.tools_types import Tools_types

admin.site.register(User)
admin.site.register(Tools)
admin.site.register(Fleet)
admin.site.register(Fleet_types)
admin.site.register(Machinery)
admin.site.register(Sites)
admin.site.register(Tools_types)