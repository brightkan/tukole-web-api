# Generated by Django 2.1.5 on 2019-05-28 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0069_usedmaterial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfleetassignment',
            name='object_type_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userfleetassignment',
            name='object_type_name',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]