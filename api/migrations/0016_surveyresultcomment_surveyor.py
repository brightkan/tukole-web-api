# Generated by Django 2.1.3 on 2018-11-12 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_sitemachines_surveyresult_surveyresultcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyresultcomment',
            name='surveyor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='surveyresultscoments_surveyor', to='api.User'),
        ),
    ]
