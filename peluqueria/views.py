from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as do_logout
from .models import Peluquero_info


def index_prueba(request):
        return render(request, "index_prueba.html")

def Cortes(request):
        return render(request, "pagina_cortes.html")

def contacto(request):
        return render(request, "contacto_prueba.html")


def profesionales(request):
    horario = Peluquero_info.objects.all()
    data = {
         'peluquero':horario
    }
    return render(request, "pagina_profesionales.html", data)










def catalogo(request):
    if request.user.is_authenticated:
        return render(request, "catalogo.html")
    return redirect('/')

def perfil(request):
 
    if request.user.is_authenticated:

        Datos_perfil = {'user': request.user}
        
        data = {
         'Datos_perfil':Datos_perfil
        }
        return render(request, "perfil.html", data)

    return redirect('/')


def informacion_peluqueria(request):
    if request.user.is_authenticated:
        return render(request, "informacion_peluqueria.html")
    return redirect('/')  

def agenda(request):
    if request.user.is_authenticated:
        horario = Peluquero_info.objects.all()
        data = {
            'peluquero':horario
        }
        return render(request, "agenda.html", data)
    return redirect('/')
