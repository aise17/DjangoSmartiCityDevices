import csv
from datetime import datetime
from pprint import pprint

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .forms import Uploadfile
from .models import Company, ScrapyTasks

from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from scrapyd_api import ScrapydAPI

from .models import ScrapyItem

scrapyd = ScrapydAPI('http://localhost:6800')


def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url)  # check if url format is valid
    except ValidationError:
        return False

    return True

def uploadURL(request):
    if request.method == 'POST' and request.FILES['path']:
        form = Uploadfile(request.POST, request.FILES)
        if form.is_valid():

            myfile = request.FILES['path']
            data = myfile.read().decode('UTF-8')
            print('ANTES {}'.format(data))

            for line in data.split():
                company = Company()
                company.name = line.split('//')[1].split('/')[0]
                company.url = line
                company.create_datetime = datetime.now()
                company.user = request.user
                company.save()
            #handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/webscrapy/dashboard/')
    elif request.method == 'GET':
        form = Uploadfile()
    return render(request, 'webscrapy/upload.html', {'form': form})


def dashboard(request):
    if request.method == 'GET':

        total_empresas = Company.objects.filter(user=request.user).count()
        lista_empresas = Company.objects.filter(user=request.user)
        lista_tareas_scrapy = ScrapyTasks.objects.filter(user=request.user)

        empresas_add_mes = Company.objects.filter(create_datetime__month=datetime.now().month, user=request.user).count()

        queryset = {
            'total_empresas': total_empresas,
            'empresas_mes': empresas_add_mes,
            'lista_empresas': lista_empresas,
            'lista_tareas_completas': lista_tareas_scrapy
        }

        return render(request, 'webscrapy/dashboard.html', queryset )





@csrf_exempt
@require_http_methods(['POST', 'GET'])  # only get and post
def crawl(request):
    # Post requests are for new crawling tasks
    if request.method == 'POST':

        url = request.POST.get('url', None)  # take url comes from client. (From an input may be?)

        if not url:
            return JsonResponse({'error': 'Missing  args'})

        if not is_valid_url(url):
            return JsonResponse({'error': 'URL is invalid'})

        domain = urlparse(url).netloc  # parse the url and extract the domain
        unique_id = str(uuid4())  # create a unique ID.
        settings = {
            'unique_id': unique_id,  # unique ID for each record for DB
            'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
        }

        scrapy_task = ScrapyTasks()
        scrapy_task.type = 'ITEMS'
        scrapy_task.status = 'LAUNCH'
        scrapy_task.user = request.user

        scrapy_task.save()

        task = scrapyd.schedule('default', 'icrawler',
                                settings=settings, url=url, domain=domain, task_id=scrapy_task.id)

        return JsonResponse({'task_id': task, 'unique_id': unique_id, 'status': 'started'})

    # Get requests are for getting result of a specific crawling task
    elif request.method == 'GET':
        task_id = request.GET.get('task_id', None)
        unique_id = request.GET.get('unique_id', None)

        if not task_id or not unique_id:
            return JsonResponse({'error': 'Missing args'})
        status = scrapyd.job_status('default', task_id)
        if status == 'finished':
            try:
                # this is the unique_id that we created even before crawling started.
                item = ScrapyItem.objects.get(unique_id=unique_id)
                return JsonResponse({'data': item.to_dict['data']})
            except Exception as e:
                return JsonResponse({'error': str(e)})
        else:
            return JsonResponse({'status': status})


def company_list(request):
    if request.method == 'GET':
        lista_empresas = Company.objects.filter(user=request.user)

        queryset = {
            'lista_empresas': lista_empresas
        }

        return render(request, 'webscrapy/company_list.html', queryset)