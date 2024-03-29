# Generated by Django 2.1.5 on 2019-05-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0058_auto_20190507_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siterole',
            name='role',
            field=models.CharField(choices=[('isp', 'ISP'), ('osp', 'OSP'), ('osp_field_manager', 'OSP Field Manager'), ('osp_supervisor', 'OSP Supervisor'), ('quality', 'Quality'), ('ofc', 'OFC'), ('driver', 'Driver'), ('surveyor', 'Surveyor'), ('project_manager', 'Project Manager'), ('fleet_manager', 'Fleet Manager'), ('mechanic', 'Mechanic'), ('fuel_station_user', 'Fuel Station User'), ('warehouse', 'warehouse'), ('garage_manager', 'Garage Manager'), ('workshop_supervisor', 'Workshop Supervisor')], max_length=150),
        ),
    ]
