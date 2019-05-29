# Generated by Django 2.1.5 on 2019-05-28 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0070_auto_20190528_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('isp', 'ISP'), ('osp', 'OSP'), ('osp_field_manager', 'OSP Field Manager'), ('osp_supervisor', 'OSP Supervisor'), ('quality', 'Quality'), ('ofc', 'OFC'), ('driver', 'Driver'), ('surveyor', 'Surveyor'), ('project_manager', 'Project Manager'), ('fleet_manager', 'Fleet Manager'), ('mechanic', 'Mechanic'), ('fuel_station_user', 'Fuel Station User'), ('warehouse', 'warehouse'), ('garage_manager', 'Garage Manager'), ('tools_head_of_department', 'Tools Head of Department'), ('tools_manager', 'Tools Manager'), ('technician', 'Technician'), ('workshop_supervisor', 'Workshop Supervisor')], max_length=150, null=True),
        ),
    ]