from django.db import models
from model_utils.models import TimeStampedModel

from api.models import Workspace, ToolType, User


# Create your models here.

class Tool(TimeStampedModel):
    status_choices = (
        ('broken', 'Broken'),
        ('healty', 'Healty'),
        ('available', 'available'),
        ('broken_down', 'broken_down'),
        ('assigned', 'assigned'),

    )
    name = models.CharField(max_length=50, null=True)
    type = models.ForeignKey(ToolType, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=50, null=True)
    humanUuid = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True, choices=status_choices)
    workspace = models.ForeignKey(to=Workspace, on_delete=models.CASCADE, null=True, blank=True,
                                  related_name="tools_workspace")
    assigned_to = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name="tools_assgined_to")


class ToolAssignment(TimeStampedModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True,
                             related_name="tools_assignment_user")
    tool = models.ForeignKey(to=Tool, on_delete=models.CASCADE, null=True, blank=True,
                             related_name="tools_assignment_tool")
