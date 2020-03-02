import uuid

from datetime import datetime as datetimee

import pika
import time
import json
import sys
import os
import django

sys.path.append('./')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSmartiCityDevices.settings")
django.setup()

from beats.models import RamDeviceHistory, ConnectionsDeviceHistory,DeviceBeatsHistory, BatteryDeviceHistory, UserDeviceHistory, RemoteDevice, GpsDevice

#from DjangoSmartiCityDevices.beats.models import RamDeviceHistory, ConnectionsDeviceHistory,DeviceBeatsHistory, BatteryDeviceHistory, UserDeviceHistory, RemoteDevice, GpsDevice
from subprocess import call

host = 'rabbitmq'
queue = 'latidos'

credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue=queue, durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')




def callback(ch, method, properties, body, datetime=None):
    print(" [x] Received %r" % body)
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    #request = json.dumps(body)
    #Do
    request = body.decode()
    with open('./request.log', 'w+') as f:
        f.write( request)
        f.close()
    jrequest: dict = json.loads(request)

    print(jrequest['cpu'])



    device_beats = DeviceBeatsHistory()
    connections_beats = ConnectionsDeviceHistory()
    user_beats = UserDeviceHistory()
    ram_beats = RamDeviceHistory()
    battery_betas = BatteryDeviceHistory()
    gps_info = GpsDevice()

    remote_device = None
    if RemoteDevice.objects.filter(device_id=jrequest['uuid']).exists():
        remote_device = RemoteDevice.objects.filter(device_id=jrequest['uuid'])[0]
    if not remote_device:
        remote_device = RemoteDevice()
        remote_device.id = uuid.uuid4()
        remote_device.device_id = jrequest['uuid']
        remote_device.create_datetime = datetimee.now()
        remote_device.save()

    device_beats.id = uuid.uuid4()
    device_beats.real_device_id = jrequest['uuid']
    device_beats.received_datetime = datetimee.now()
    device_beats.device_datetime = jrequest['datetime']
    device_beats.operation_system = jrequest['so']
    device_beats.image = jrequest['image']
    device_beats.cpu_usage = jrequest['cpu']
    device_beats.received_datetime = datetimee.now()
    device_beats.remote_device_id = remote_device

    print('BATTERY {}'.format(jrequest['battery'][0]))
    battery_betas.id = uuid.uuid4()
    battery_betas.received_datetime = datetimee.now()
    battery_betas.percent = jrequest['battery'][0]
    battery_betas.secsleft = jrequest['battery'][1]
    battery_betas.power_plugged = jrequest['battery'][2]
    battery_betas.remote_device_id = remote_device

    battery_betas.save()

    print('RAM {}'.format(jrequest['ram']['total']))
    ram_beats.id = uuid.uuid4()
    ram_beats.received_datetime = datetimee.now()
    ram_beats.total = jrequest['ram']['total']
    ram_beats.available = jrequest['ram']['available']
    ram_beats.percent = jrequest['ram']['percent']
    ram_beats.used = jrequest['ram']['used']
    ram_beats.free = jrequest['ram']['free']
    ram_beats.remote_device_id = remote_device

    ram_beats.save()

    print('USER {}'.format(jrequest['user'][0]))
    user_beats.id = uuid.uuid4()
    user_beats.received_datetime = datetimee.now()
    user_beats.name = jrequest['user'][0][0]
    user_beats.terminal = jrequest['user'][0][1]
    user_beats.host = jrequest['user'][0][2]
    user_beats.started = jrequest['user'][0][3]
    user_beats.remote_device_id = remote_device
    if jrequest['user'][0][4]:
        user_beats.pid = jrequest['user'][0][4]
    else:
        user_beats.pid = 0
    user_beats.save()


    print('CONNECTIONS 0 5 {}'.format(jrequest['connections'][0][5]))
    print('CONNECTIONS 0 6 {}'.format(jrequest['connections'][0][6]))
    connections_beats.id = uuid.uuid4()
    connections_beats.remote_device_id = remote_device
    connections_beats.received_datetime = datetimee.now()
    connections_beats.fd = jrequest['connections'][0][0]
    connections_beats.family = jrequest['connections'][0][1]
    connections_beats.type = jrequest['connections'][0][2]
    connections_beats.laddr = '{}:{}'.format(str(jrequest['connections'][0][3][0]), str(jrequest['connections'][0][3][1]))
    if jrequest['connections'][0][4]:
        print('CONNECTIONS 0 4 0 {}'.format(jrequest['connections'][0][4][0]))
        print('CONNECTIONS 0 4 {}'.format(jrequest['connections'][0][4]))
        connections_beats.raddr = '{}:{}'.format(str(jrequest['connections'][0][4][0]), str(jrequest['connections'][0][4][1]))
    connections_beats.status = jrequest['connections'][0][5]
    connections_beats.status = jrequest['connections'][0][6]

    connections_beats.save()


    print(jrequest['gpsinfo']['latlng'][0])
    gps_info.id = uuid.uuid4()
    gps_info.received_datetime = datetimee.now()
    gps_info.remote_device_id = remote_device
    gps_info.city = jrequest['gpsinfo']['city']
    gps_info.lat = jrequest['gpsinfo']['latlng'][0]
    gps_info.long = jrequest['gpsinfo']['latlng'][1]

    gps_info.save()


    device_beats.connections = connections_beats
    device_beats.user = user_beats
    device_beats.ram_usage = ram_beats
    device_beats.battery_usage = battery_betas
    device_beats.gps_info =gps_info

    ok = device_beats.save()

   # print('ok ' + str(ok))

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue, on_message_callback=callback)

channel.start_consuming()
