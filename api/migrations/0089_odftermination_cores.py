# Generated by Django 2.1.5 on 2019-09-16 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0088_siteimage_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='odftermination',
            name='cores',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
