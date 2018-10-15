# Generated by Django 2.1.2 on 2018-10-15 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181012_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('uuid', models.CharField(max_length=50, null=True)),
                ('humanUuid', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fleet_types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Machinery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('uuid', models.CharField(max_length=50, null=True)),
                ('humanUuid', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('ackStatus', models.BooleanField(default=False)),
                ('workStatus', models.CharField(max_length=50, null=True)),
                ('archivedStatus', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateField(null=True)),
                ('updated_at', models.DateField(null=True)),
                ('clientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('uuid', models.CharField(max_length=50, null=True)),
                ('humanUuid', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tools_types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='tools',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Tools_types'),
        ),
        migrations.AddField(
            model_name='fleet',
            name='vehicle_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Fleet_types'),
        ),
    ]