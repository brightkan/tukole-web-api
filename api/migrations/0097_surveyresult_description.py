# Generated by Django 2.1.5 on 2019-10-07 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0096_auto_20191007_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyresult',
            name='description',
            field=models.TextField(default=False),
        ),
    ]