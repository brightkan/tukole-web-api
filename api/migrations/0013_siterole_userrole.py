# Generated by Django 2.1.3 on 2018-11-08 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_userroles'),
    ]

    operations = [
        migrations.AddField(
            model_name='siterole',
            name='userrole',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='siterole_userrole', to='api.UserRoles'),
        ),
    ]