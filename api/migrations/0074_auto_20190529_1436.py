# Generated by Django 2.1.5 on 2019-05-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0073_activity_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfleetassignment',
            name='object_type_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
