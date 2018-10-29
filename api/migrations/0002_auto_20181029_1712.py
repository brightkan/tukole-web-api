# Generated by Django 2.1.2 on 2018-10-29 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fleet',
            name='workspace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fleet_workspace', to='api.Workspace'),
        ),
        migrations.AddField(
            model_name='machinery',
            name='workspace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='machinery_workspace', to='api.Workspace'),
        ),
        migrations.AddField(
            model_name='material',
            name='workspace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='material_workspace', to='api.Workspace'),
        ),
    ]
