# Generated by Django 2.1.5 on 2019-03-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20190321_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='site_usd_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
