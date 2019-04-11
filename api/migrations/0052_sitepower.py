# Generated by Django 2.1.5 on 2019-04-11 07:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0051_auto_20190411_0840'),
    ]

    operations = [
        migrations.CreateModel(
            name='SitePower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('material_used', models.CharField(blank=True, max_length=255, null=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.BooleanField(blank=True, null=True)),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Site')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
