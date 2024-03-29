# Generated by Django 3.0.1 on 2019-12-29 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryDeviceHistory',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('received_datetime', models.DateTimeField(auto_now=True)),
                ('percent', models.FloatField()),
                ('secsleft', models.CharField(blank=True, max_length=255, null=True)),
                ('power_plugged', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ConnectionsDeviceHistory',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('received_datetime', models.DateTimeField(auto_now=True)),
                ('fd', models.CharField(blank=True, max_length=255, null=True)),
                ('family', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('laddr', models.CharField(blank=True, max_length=255, null=True)),
                ('raddr', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('pid_device', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RemoteDevice',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('device_id', models.UUIDField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('create_datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDeviceHistory',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('received_datetime', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('terminal', models.CharField(blank=True, max_length=255, null=True)),
                ('host', models.CharField(blank=True, max_length=255, null=True)),
                ('started', models.BigIntegerField()),
                ('pid', models.BigIntegerField()),
                ('remote_device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beats.RemoteDevice')),
            ],
        ),
        migrations.CreateModel(
            name='RamDeviceHistory',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('received_datetime', models.DateTimeField(auto_now=True)),
                ('total', models.BigIntegerField()),
                ('available', models.BigIntegerField()),
                ('percent', models.FloatField()),
                ('used', models.BigIntegerField()),
                ('free', models.BigIntegerField()),
                ('remote_device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beats.RemoteDevice')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceBeatsHistory',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('received_datetime', models.DateTimeField(auto_now=True)),
                ('device_datetime', models.DateTimeField()),
                ('operation_system', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('cpu_usage', models.FloatField()),
                ('battery_usage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beats.BatteryDeviceHistory')),
                ('connections', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beats.ConnectionsDeviceHistory')),
                ('ram_usage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beats.RamDeviceHistory')),
                ('remote_device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beats.RemoteDevice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beats.UserDeviceHistory')),
            ],
        ),
        migrations.AddField(
            model_name='connectionsdevicehistory',
            name='remote_device_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beats.RemoteDevice'),
        ),
        migrations.AddField(
            model_name='batterydevicehistory',
            name='remote_device_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beats.RemoteDevice'),
        ),
    ]
