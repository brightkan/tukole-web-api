# Generated by Django 2.1.3 on 2018-11-26 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20181123_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='destination',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='start',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]