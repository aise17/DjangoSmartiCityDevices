from django.db import models

# Create your models here.
from django.shortcuts import render

# Create your views here.

from django.db import models


class RemoteDevice(models.Model):
    id = models.UUIDField(primary_key=True)
    device_id = models.UUIDField()
    name = models.CharField(null=True, blank=True, max_length=255)
    create_datetime = models.DateTimeField(auto_now=True)



class ConnectionsDeviceHistory(models.Model):
    id = models.UUIDField(primary_key=True)
    received_datetime = models.DateTimeField(auto_now=True)
    fd = models.CharField(null=True, blank=True, max_length=255)
    family = models.CharField(null=True, blank=True, max_length=255)
    type = models.CharField(null=True, blank=True, max_length=255)
    laddr = models.CharField(null=True, blank=True, max_length=255)
    raddr = models.CharField(null=True, blank=True, max_length=255)
    status = models.CharField(null=True, blank=True, max_length=255)
    pid_device = models.CharField(null=True, blank=True, max_length=255)
    remote_device_id = models.ForeignKey(RemoteDevice, on_delete=models.CASCADE)



class RamDeviceHistory(models.Model):
    id = models.UUIDField(primary_key=True)
    received_datetime = models.DateTimeField(auto_now=True)
    total = models.BigIntegerField()
    available = models.BigIntegerField()
    percent = models.FloatField()
    used = models.BigIntegerField()
    free = models.BigIntegerField()
    remote_device_id = models.ForeignKey(RemoteDevice, on_delete=models.CASCADE)



class BatteryDeviceHistory(models.Model):
    id = models.UUIDField(primary_key=True)
    received_datetime = models.DateTimeField(auto_now=True)
    percent = models.FloatField()
    secsleft = models.CharField(null=True, blank=True, max_length=255)
    power_plugged = models.BooleanField()
    remote_device_id = models.ForeignKey(RemoteDevice, on_delete=models.CASCADE)



class UserDeviceHistory(models.Model):
    id = models.UUIDField(primary_key=True)
    received_datetime = models.DateTimeField(auto_now=True)
    name = models.CharField(null=True, blank=True, max_length=255)
    terminal = models.CharField(null=True, blank=True, max_length=255)
    host = models.CharField(null=True, blank=True, max_length=255)
    started = models.BigIntegerField()
    pid = models.BigIntegerField()
    remote_device_id = models.ForeignKey(RemoteDevice, on_delete=models.CASCADE)
    

class GpsDevice(models.Model):
    id = models.UUIDField(primary_key=True)
    received_datetime = models.DateTimeField(auto_now=True)
    city = models.CharField(null=True, blank=True, max_length=255)
    lat = models.CharField(null=True, blank=True, max_length=255)
    long = models.CharField(null=True, blank=True, max_length=255)
    remote_device_id = models.ForeignKey(RemoteDevice, on_delete=models.CASCADE, default=None)


class DeviceBeatsHistory (models.Model):
    id = models.UUIDField(primary_key=True)
    received_datetime = models.DateTimeField(auto_now=True)
    device_datetime = models.DateTimeField()
    operation_system = models.CharField(null=True, blank=True, max_length=255)
    image = models.TextField(null=True, blank=True)
    cpu_usage = models.FloatField()
    connections = models.ForeignKey(ConnectionsDeviceHistory, on_delete=models.CASCADE)
    ram_usage = models.ForeignKey(RamDeviceHistory, on_delete=models.CASCADE)
    battery_usage = models.ForeignKey(BatteryDeviceHistory, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDeviceHistory, on_delete=models.CASCADE)
    remote_device_id = models.ForeignKey(RemoteDevice, on_delete=models.CASCADE)
    gps_info = models.ForeignKey(GpsDevice, on_delete=models.CASCADE, default=None)

