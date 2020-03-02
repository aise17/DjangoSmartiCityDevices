import csv
from datetime import datetime
from pprint import pprint

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .forms import Uploadfile
from .models import Company


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
                company.save()
            #handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/wescrapy/uploadURL')
    elif request.method == 'GET':
        form = Uploadfile()
    return render(request, 'webscrapy/upload.html', {'form': form})


def dashboard(request):
    if request.method == 'GET':

        total_empresas = Company.objects.all().count()
        lista_empresas = Company.objects.all()

        empresas_add_mes = Company.objects.filter(create_datetime__month=datetime.now().month).count()

        queryset = {
            'total_empresas': total_empresas,
            'empresas_mes': empresas_add_mes,
            'lista_empresas': lista_empresas
        }

        return render(request, 'webscrapy/dashboard.html', queryset )