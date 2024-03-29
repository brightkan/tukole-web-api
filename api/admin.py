from django.contrib import admin

# Register your models here.
from api.models import (
    User,
    Fleet,
    Machinery,
    ToolType,
    Site,
    Workspace,
    Material,
    FleetCheckList,
    FleetCheckListItem,
    FleetFuelRequest,
    ManHole,
    ManHoleAssignment,
    UserPerformanceMetric,
    Metric,
    SiteWorkStatus,
    FleetCheckListItemResult,
    UsedMaterial,
    SiteImage,
)
from api.models.fleet_types import FleetType
from api.models.fleets import UserFleetAssignment
from api.models.manholes import ODFTerminationTool, ODFTermination
from api.models.repairs import RepairTicket
from api.models.siteboqs import Siteboq
from api.models.siteroles import Siterole
from api.models.survey_result_comments import SurveyResultComment
from api.models.survey_results import SurveyResult
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
admin.site.register(Siteboq)
admin.site.register(Material)
admin.site.register(UsedMaterial)
admin.site.register(UserWorkSpace)
admin.site.register(Siterole)
admin.site.register(SurveyResult)
admin.site.register(SurveyResultComment)
admin.site.register(FleetCheckList)
admin.site.register(FleetCheckListItem)
admin.site.register(UserFleetAssignment)
admin.site.register(FleetCheckListItemResult)
admin.site.register(FleetFuelRequest)
admin.site.register(ManHole)
admin.site.register(ManHoleAssignment)
admin.site.register(UserPerformanceMetric)
admin.site.register(Metric)
admin.site.register(SiteWorkStatus)
admin.site.register(RepairTicket)
admin.site.register(SiteImage)
admin.site.register(ODFTermination)
admin.site.register(ODFTerminationTool)
