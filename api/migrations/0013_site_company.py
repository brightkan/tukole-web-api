# Generated by Django 2.1.3 on 2019-01-17 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Company'),
        ),
    ]
