# Generated by Django 2.1.2 on 2018-11-02 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_siteboq_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteboq',
            name='actual_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='siteboq',
            name='estimate_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
