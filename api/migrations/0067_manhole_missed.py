# Generated by Django 2.1.5 on 2019-05-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0066_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='manhole',
            name='missed',
            field=models.BooleanField(default=False),
        ),
    ]
