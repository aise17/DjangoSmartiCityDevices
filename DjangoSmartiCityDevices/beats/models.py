from django.db import models

# Create your models here.
from django.shortcuts import render

# Create your views here.

from django.db import models





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



class RamDeviceHistory(models.Model):
    id = models.UUIDField(primary_key=True)
    received_datetime = models.DateTimeField(auto_now=True)
    total = models.BigIntegerField()
    available = models.BigIntegerField()
    percent = models.FloatField()
    used = models.BigIntegerField()
    free = models.BigIntegerField()



class BatteryDeviceHistory(models.Model):
    id = models.UUIDField(primary_key=True)
    received_datetime = models.DateTimeField(auto_now=True)
    percent = models.FloatField()
    secsleft = models.CharField(null=True, blank=True, max_length=255)
    power_plugged = models.BooleanField()



class UserDeviceHistory(models.Model):
    id = models.UUIDField(primary_key=True)
    received_datetime = models.DateTimeField(auto_now=True)
    name = models.CharField(null=True, blank=True, max_length=255)
    terminal = models.CharField(null=True, blank=True, max_length=255)
    host = models.CharField(null=True, blank=True, max_length=255)
    started = models.BigIntegerField()
    pid = models.BigIntegerField()



class DeviceBeatsHistory (models.Model):
    id = models.UUIDField(primary_key=True)
    real_device_id = models.UUIDField()
    received_datetime = models.DateTimeField(auto_now=True)
    device_datetime = models.DateTimeField()
    operation_system = models.CharField(null=True, blank=True, max_length=255)
    image = models.TextField(null=True, blank=True)
    cpu_usage = models.FloatField()
    connections = models.ForeignKey(ConnectionsDeviceHistory, on_delete=models.CASCADE)
    ram_usage = models.ForeignKey(RamDeviceHistory, on_delete=models.CASCADE)
    battery_usage = models.ForeignKey(BatteryDeviceHistory, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDeviceHistory, on_delete=models.CASCADE)

