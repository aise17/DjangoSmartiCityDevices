import json
from pprint import pformat
from .models import *

from django.http import JsonResponse
from django.shortcuts import render
from .tasks import celery_taskA

# Create your views here.
from django.shortcuts import HttpResponse

def celery_view(request):
    for counter in range(2):
        celery_taskA.delay(counter)
    return render(request, 'security/base.html')


def worker_list(request):
    data = dict()
    from celery.events import EventReceiver

    return JsonResponse(data, safe=False)


def device_list(request):
    if request.method == 'GET':
        response = dict()
        list_devices = RemoteDevice.objects.all()
        print(list_devices)
        response['list_devices'] = list_devices

        return render(request,'beats/dashboard.html', {'question': list_devices})

    elif request.method == 'POST':
        pass
