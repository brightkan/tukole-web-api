# Generated by Django 2.1.5 on 2019-05-07 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0057_odftermination'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteimage',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='siteimage',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
