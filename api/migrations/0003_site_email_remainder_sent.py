# Generated by Django 2.1.3 on 2019-01-08 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190103_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='email_remainder_sent',
            field=models.BooleanField(default=False),
        ),
    ]
