from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from api.views.users import UserViewSet

from api.views.fleet_types import Fleet_typesViewset as myapp_fleet_types_views

from api.views.fleets import FleetViewset as myapp_fleets_views
from api.views.machinerys import MachineryViewset as myapp_machinerys_views
from api.views.tools_types import Tools_typesViewset as myapp_tools_types_views
from api.views.tools import ToolsViewset as myapp_tools_views
from api.views.sites import SitesViewset as myapp_sites_views


#router
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')

router.register(r'fleet_types', myapp_fleet_types_views)
router.register(r'fleets', myapp_fleets_views)
router.register(r'machinerys', myapp_machinerys_views)
router.register(r'tools_types', myapp_tools_types_views)
router.register(r'tools', myapp_tools_views)
router.register(r'sites', myapp_sites_views)

#swagger_view
schema_view = get_swagger_view(title='Tukole API')

urlpatterns = [
    path('docs/', schema_view),
    path('', include(router.urls)),

]
