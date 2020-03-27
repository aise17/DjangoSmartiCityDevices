import json
from pprint import pformat

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from django.contrib.auth.models import User, Group
from django.contrib import admin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, GroupSerializer, UserLoginSerializer

admin.autodiscover()
from rest_framework import generics, permissions, serializers, views, status
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.decorators import permission_classes

from .tasks import celery_task

def index(request):
    for counter in range(2):
        celery_task.delay(counter)
    return render(request, 'security/index.html')

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')
                # Si llegamos al final renderizamos el formulario
    return render(request, "security/login.html", {'form': form})


def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "security/register.html", {'form': form})

def logout(request):
    do_logout(request)
    return redirect('/')

def worker_list(request):
    data = dict()
    from celery.events import EventReceiver

    return JsonResponse(data , safe=False)

@permission_classes([AllowAny])
class LoginApi(generics.ListCreateAPIView):

    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):

        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():

            salida = dict()

            user = authenticate(username=serializer['username'].value, password=serializer['password'].value)
            if user:
                login(request)
                ser = UserSerializer(instance=user)

                salida['ok'] = True
                salida['datos'] = ser.data
            else:
                salida['ok'] = False
                salida['error'] = 'fallo en la autentificacion'

            return JsonResponse(salida, status=status.HTTP_200_OK)





# Create the API views
class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer