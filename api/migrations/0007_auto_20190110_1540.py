# Generated by Django 2.1.3 on 2019-01-10 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_site_site_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleet',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('broken_down', 'broken_down'), ('assigned', 'assigned')], max_length=150, null=True),
        ),
    ]
