# Generated by Django 2.1.3 on 2018-11-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20181112_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
