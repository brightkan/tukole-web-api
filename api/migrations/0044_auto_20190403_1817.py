# Generated by Django 2.1.5 on 2019-04-03 15:17

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0043_auto_20190403_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='fleetfuelrequest',
            name='humanUuid',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
