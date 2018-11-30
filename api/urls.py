from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from api.views.challenge import ChallengeViewset
from api.views.comment import CommentViewSet
from api.views.fleet_types import Fleet_typesViewset as myapp_fleet_types_views
from api.views.fleets import FleetViewset as myapp_fleets_views
from api.views.machinery import MachineryViewset as myapp_machinerys_views
from api.views.machinery_types import MachineryTypeViewset as myapp_machinery_types_views
from api.views.manholes import ManHoleViewSet
from api.views.materials import MaterialViewSet
from api.views.notifications import NotificationViewset as myapp_notifications_views
from api.views.siteboqs import SiteboqViewSet as myapp_siteboqs_views
from api.views.sitefleets import SitefleetViewSet as myapp_sitefleets_views, UserSitefleetViewSet
from api.views.sitemachines import SiteMachinesViewSet as myapp_sitemachines_views
from api.views.sitereports import SitereportViewSet as myapp_sitereports_views
from api.views.siteroles import SiteroleViewSet as myapp_siteroles_views
from api.views.sites import SitesViewset as myapp_sites_views
from api.views.sitestatuses import SitestatusViewSet as myapp_sitestatus_views
from api.views.sitetools import SitetoolViewSet as myapp_sitetools_views
from api.views.survey_result_comments import SurveyResultCommentViewSet as myapp_survey_result_comments_views
from api.views.survey_results import SurveyResultViewSet as myapp_survey_results_views
from api.views.surveys import SurveyViewset as myapp_surveys_views
from api.views.tools import ToolsViewset as myapp_tools_views
from api.views.tools_types import Tools_typesViewset as myapp_tools_types_views
from api.views.trips import TripViewSet
from api.views.user_roles import UserRolesViewSet as myapp_user_roles_views
from api.views.users import UserViewSet
from api.views.userworkspaces import UserWorkSpaceViewSet
from api.views.warehousematerials import WarehouseMaterialViewset as myapp_warehousematerials_views
from api.views.workspaces import WorkspaceViewset as myapp_workspaces_views

# router
router = routers.DefaultRouter()
router.register(r'challenges', ChallengeViewset, base_name='challenges')
router.register(r'users', UserViewSet, base_name='users')
router.register(r'materials', MaterialViewSet, base_name='materials')
router.register(r'comments', CommentViewSet, base_name='comments')
router.register(r'workspaces', myapp_workspaces_views)
router.register(r'userworkspaces', UserWorkSpaceViewSet, base_name='user_workspaces')
router.register(r'fleet_types', myapp_fleet_types_views)
router.register(r'fleets', myapp_fleets_views)
router.register(r'machinery', myapp_machinerys_views)
router.register(r'tools_types', myapp_tools_types_views)
router.register(r'tools', myapp_tools_views)
router.register(r'sites', myapp_sites_views)
router.register(r'siteboqs', myapp_siteboqs_views)
router.register(r'sitefleets', myapp_sitefleets_views)
router.register(r'usersitefleets', UserSitefleetViewSet, base_name="user-site-fleet")
router.register(r'sitereports', myapp_sitereports_views)
router.register(r'siteroles', myapp_siteroles_views)
router.register(r'sitestatus', myapp_sitestatus_views)
router.register(r'sitetools', myapp_sitetools_views)
router.register(r'trips', TripViewSet, base_name='trips')
router.register(r'machinery_types', myapp_machinery_types_views)
router.register(r'manholes', ManHoleViewSet, base_name="man-holes")
router.register(r'surveys', myapp_surveys_views)
router.register(r'notifications', myapp_notifications_views)
router.register(r'warehousematerials', myapp_warehousematerials_views)
router.register(r'user_roles', myapp_user_roles_views)
router.register(r'sitemachines', myapp_sitemachines_views)
router.register(r'survey_results', myapp_survey_results_views)
router.register(r'survey_result_comments', myapp_survey_result_comments_views)

# swagger_view
schema_view = get_swagger_view(title='Tukole API')

urlpatterns = [
    path('docs/', schema_view),
    path('', include(router.urls)),

]
