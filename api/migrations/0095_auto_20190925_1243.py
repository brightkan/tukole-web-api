# Generated by Django 2.1.5 on 2019-09-25 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0094_auto_20190925_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='odfinstallation',
            old_name='install_confirmed',
            new_name='odf_install_confirmed',
        ),
    ]
