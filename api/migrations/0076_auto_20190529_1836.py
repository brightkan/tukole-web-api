# Generated by Django 2.1.5 on 2019-05-29 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0075_fleetchecklistitemresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fleetchecklistitemresult',
            name='request_object_type',
        ),
        migrations.AlterField(
            model_name='fleetchecklistitemresult',
            name='fleet_check_list_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.FleetCheckListItem'),
        ),
        migrations.AlterField(
            model_name='fleetchecklistitemresult',
            name='request_object_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.UserFleetAssignment'),
        ),
    ]
