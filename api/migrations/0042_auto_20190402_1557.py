# Generated by Django 2.1.5 on 2019-04-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_material_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
    ]