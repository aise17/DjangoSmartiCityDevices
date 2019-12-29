import json
from pprint import pformat

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

from .tasks import celery_task

def celery_view(request):
    for counter in range(2):
        celery_task.delay(counter)
    return render(request, 'security/base.html')


def worker_list(request):
    data = dict()
    from celery.events import EventReceiver

    return JsonResponse(data , safe=False)