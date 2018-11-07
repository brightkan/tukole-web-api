# Generated by Django 2.1.3 on 2018-11-07 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_warehousematerial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='ack_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='ack_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='site_ack_user', to='api.User'),
        ),
        migrations.AddField(
            model_name='site',
            name='site_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='site',
            name='surveyor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='site_surveyor', to='api.User'),
        ),
    ]
