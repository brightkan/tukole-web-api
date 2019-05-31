# Generated by Django 2.1.5 on 2019-05-31 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0079_auto_20190530_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='survay_time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='siteimage',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=12, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='siteimage',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=12, max_digits=12, null=True),
        ),
    ]