# Generated by Django 2.1.5 on 2019-07-30 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0086_auto_20190730_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='roadcrossing',
            name='machinery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Machinery'),
        ),
        migrations.AlterField(
            model_name='roadcrossing',
            name='tool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Tool'),
        ),
    ]
