# Generated by Django 2.1.5 on 2019-05-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0072_userfleetassignment_approved_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='duration',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
