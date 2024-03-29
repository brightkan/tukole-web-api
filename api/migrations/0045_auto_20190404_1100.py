# Generated by Django 2.1.5 on 2019-04-04 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_auto_20190403_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairticket',
            name='acknowledged_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repair_acknowledged_by', to='api.User'),
        ),
        migrations.AddField(
            model_name='repairticket',
            name='assessment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='repairticket',
            name='mechanic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repair_mechanic', to='api.User'),
        ),
        migrations.AddField(
            model_name='repairticket',
            name='object_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='repairticket',
            name='repairs_complete',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='repairticket',
            name='repairs_complete_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='repairticket',
            name='reported_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repair_reported_by', to='api.User'),
        ),
        migrations.AddField(
            model_name='repairticket',
            name='requisition_ended',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='repairticket',
            name='requisition_materials',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='repairticket',
            name='requisition_started',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='repairticket',
            name='supervised_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repair_supervised_by', to='api.User'),
        ),
        migrations.AddField(
            model_name='repairticket',
            name='time_acknowledged',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='repairticket',
            name='time_reported',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='repairticket',
            name='type',
            field=models.CharField(blank=True, choices=[('machine', 'Machine'), ('tool', 'Tool'), ('fleet', 'Fleet')], max_length=255, null=True),
        ),
    ]
