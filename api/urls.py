from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from api.views.challenge import ChallengeViewset
from api.views.comment import CommentViewSet
from api.views.company import CompanyViewSet
from api.views.cost import CostViewSet
from api.views.distance import TrenchedDistanceViewSet
from api.views.fleet_check_list import FleetCheckListItemViewset, FleetCheckListViewset
from api.views.fleet_types import Fleet_typesViewset as myapp_fleet_types_views
from api.views.fleets import FleetViewset, UserFleetAssignmentViewSet
from api.views.fuel import FuelViewSet, FleetFuelRequestViewSet, FuelReceiptViewSet
from api.views.history import ToolHistoryViewSet, MachineHistoryViewSet, FleetHistoryViewSet
from api.views.incidents import IncidentViewSet
from api.views.machinery import MachineryViewset as myapp_machinerys_views
from api.views.machinery_types import MachineryTypeViewset as myapp_machinery_types_views
from api.views.manholes import ManHoleViewSet, ManHoleAssignmentViewSet, ManHoleInstallationViewSet, \
    HandHoleInstallationViewSet
from api.views.materials import MaterialViewSet
from api.views.metrics import MetricViewSet, UserPerformanceMetricViewSet
from api.views.notifications import NotificationViewset as myapp_notifications_views
from api.views.reinstallation import ReInstallationViewSet
from api.views.repairs import RepairHistoryViewSet, RepairTicketViewSet
from api.views.roadcrossing import RoadCrossingViewSet
from api.views.siteboqs import SiteboqViewSet as myapp_siteboqs_views
from api.views.sitefleets import SitefleetViewSet as myapp_sitefleets_views, UserSitefleetViewSet
from api.views.sitemachines import SiteMachinesViewSet as myapp_sitemachines_views
from api.views.sitereports import SitereportViewSet as myapp_sitereports_views
from api.views.siteroles import SiteroleViewSet as myapp_siteroles_views
from api.views.sites import SitesViewset as myapp_sites_views, SiteImageViewSet, SiteDocumentViewSet, SitePIPViewSet, \
    SitePoweringViewSet
from api.views.sitestatuses import SitestatusViewSet as myapp_sitestatus_views
from api.views.sitetools import SitetoolViewSet as myapp_sitetools_views
from api.views.siteworktimes import SiteArrivalTimeViewSet, SiteWorkStatusViewSet
from api.views.survey_result_comments import SurveyResultCommentViewSet as myapp_survey_result_comments_views
from api.views.survey_results import SurveyResultViewSet as myapp_survey_results_views
from api.views.surveys import SurveyViewset as myapp_surveys_views
from api.views.tools import ToolsViewset as myapp_tools_views, ToolAssignmentViewSet
from api.views.tools_types import Tools_typesViewset as myapp_tools_types_views
from api.views.trips import TripViewSet, RouteChangeViewSet, OtherViewSet
from api.views.user_roles import UserRolesViewSet as myapp_user_roles_views
from api.views.users import UserViewSet
from api.views.userworkspaces import UserWorkSpaceViewSet
from api.views.warehousematerials import WarehouseMaterialViewset as myapp_warehousematerials_views
from api.views.workspaces import WorkspaceViewset as myapp_workspaces_views

# router
router = routers.DefaultRouter()
router.register(r'challenges', ChallengeViewset, base_name='challenges')
router.register(r'company', CompanyViewSet, base_name='companies')
router.register(r'users', UserViewSet, base_name='users')
router.register(r'materials', MaterialViewSet, base_name='materials')
router.register(r'comments', CommentViewSet, base_name='comments')
router.register(r'cost', CostViewSet, base_name='cost')
router.register(r'workspaces', myapp_workspaces_views)
router.register(r'userworkspaces', UserWorkSpaceViewSet, base_name='user_workspaces')
router.register(r'fleet_types', myapp_fleet_types_views)
router.register(r'fleets', FleetViewset, base_name='fleets')
router.register(r'fuels', FuelViewSet, base_name='fuel')
router.register(r'fleetfuelrequest', FleetFuelRequestViewSet, base_name='fleet-fuel-request')
router.register(r'fleetfuelreceipt', FuelReceiptViewSet, base_name='fleet-fuel-receipt')
router.register(r'fleethistory', FleetHistoryViewSet, base_name='fleet-history')
router.register(r'machinehistory', MachineHistoryViewSet, base_name='machine-history')
router.register(r'toolhistory', ToolHistoryViewSet, base_name='tool-history')
router.register(r'fleetchecklist', FleetCheckListViewset, base_name='fleet-check-list')
router.register(r'fleetchecklistitems', FleetCheckListItemViewset, base_name='fleet-check-list-items')
router.register(r'machinery', myapp_machinerys_views)
router.register(r'tools_types', myapp_tools_types_views)
router.register(r'tools', myapp_tools_views)
router.register(r'toolsassignments', ToolAssignmentViewSet, base_name='tool-assignment')
router.register(r'sites', myapp_sites_views)
router.register(r'sitesimages', SiteImageViewSet, base_name='site-images')
router.register(r'sitesdocuments', SiteDocumentViewSet, base_name='site-document')
router.register(r'sitespips', SitePIPViewSet, base_name='site-pips')
router.register(r'sitearrivaltimes', SiteArrivalTimeViewSet, base_name='site-arrival-times')
router.register(r'siteworkstatus', SiteWorkStatusViewSet, base_name='site-work-status')
router.register(r'sitepowering', SitePoweringViewSet, base_name='site-powering')
router.register(r'siteboqs', myapp_siteboqs_views)
router.register(r'sitefleets', myapp_sitefleets_views)
router.register(r'routechange', RouteChangeViewSet, base_name='route-change')
router.register(r'other', OtherViewSet, base_name='other-viewset')
router.register(r'usersitefleets', UserSitefleetViewSet, base_name="user-site-fleet")
router.register(r'userfleetsassignments', UserFleetAssignmentViewSet, base_name="user-fleet-assignments")
router.register(r'sitereports', myapp_sitereports_views)
router.register(r'siteroles', myapp_siteroles_views)
router.register(r'sitestatus', myapp_sitestatus_views)
router.register(r'sitetools', myapp_sitetools_views)
router.register(r'trips', TripViewSet, base_name='trips')
router.register(r'machinery_types', myapp_machinery_types_views)
router.register(r'metrics', MetricViewSet, base_name="metrics")
router.register(r'usermetrics', UserPerformanceMetricViewSet, base_name="user-metric")
router.register(r'manholes', ManHoleViewSet, base_name="man-holes")
router.register(r'manholesassignment', ManHoleAssignmentViewSet, base_name="man-assignments")
router.register(r'manholesinstallation', ManHoleInstallationViewSet, base_name="manhole-installments")
router.register(r'handholeinstallation', HandHoleInstallationViewSet, base_name="handhole-installments")
router.register(r'roadcrossing', RoadCrossingViewSet, base_name="road-crossing")
router.register(r'reinstallation', ReInstallationViewSet, base_name="reinstallation")
router.register(r'repairhistory', RepairHistoryViewSet, base_name="repair-history")
router.register(r'repairticket', RepairTicketViewSet, base_name="repair-ticket")
router.register(r'distance/trenched', TrenchedDistanceViewSet, base_name="distance-trenched")
router.register(r'incidents', IncidentViewSet, base_name="site-incident")
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
