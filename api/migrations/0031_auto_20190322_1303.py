# Generated by Django 2.1.5 on 2019-03-22 10:03

import api.models.fleets
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_handholeinstallation_manholeinstallation'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFleetAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('assignment_type', models.CharField(blank=True, choices=[('assignment', 'Assignment'), ('request', 'Request')], max_length=150, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('approved', models.BooleanField(default=api.models.fleets.Fleet)),
                ('fleet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Fleet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='fleetfuelrequest',
            old_name='total_fuel_amount',
            new_name='fuel_amount',
        ),
        migrations.AddField(
            model_name='fleetfuelrequest',
            name='allow_full_tank',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fleetfuelrequest',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fleetfuelrequest',
            name='pump_screenshot',
            field=models.FileField(blank=True, null=True, upload_to='fuel/screenshot'),
        ),
        migrations.AddField(
            model_name='fleetfuelrequest',
            name='type',
            field=models.CharField(blank=True, choices=[('machine', 'Machine'), ('fleet', 'Fleet')], max_length=155, null=True),
        ),
        migrations.AlterField(
            model_name='fleetfuelrequest',
            name='fleet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Fleet'),
        ),
    ]