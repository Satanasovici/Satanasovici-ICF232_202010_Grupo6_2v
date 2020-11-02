from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as do_logout
from .models import Peluquero_info, servicios, peluqueros, peluqueros_servicios, peluquero_horas, horas_peluqueria, fecha
from datetime import date
from datetime import datetime
from django.utils import timezone, dateformat
from django.db.models import Count
from django.http import JsonResponse


def Editar_Perfil(request):
        return render(request, "Editar_Perfil.html")


def index_prueba(request):
        return render(request, "index_prueba.html")

def Cortes(request):
        return render(request, "pagina_cortes.html")


def Alisados(request):
        return render(request, "pagina_alisados.html")


def Tintes(request):
        return render(request, "pagina_tintes.html")


def Afeitados(request):
        return render(request, "pagina_afeitados.html")


def Lavados(request):
        return render(request, "pagina_lavados.html")


def Peinados(request):
        return render(request, "pagina_peinados.html")









def profesionales(request):
    horario = Peluquero_info.objects.all()
    data = {
         'peluquero':horario
    }
    return render(request, "pagina_profesionales.html", data)


def contacto(request):
        return render(request, "contacto_prueba.html")






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





############################################################################################################
    



def seleccionar_peluquero (request, cod):

    peluqueros = peluqueros_servicios.objects.all()

    return render (request, "seleccionar_peluquero.html", {
        'peluqueros':peluqueros,
        'cod':cod
    })


def seleccionar_hora (request,cod,cod2):

   
    horas = peluquero_horas.objects.all()
    horario = horas_peluqueria.objects.all()
    

    return render (request, "ver_horas.html", {
        'horas':horas,
        'cod':cod,
        'cod2':cod2,
        'horario':horario
    })




def seleccionar_fecha (request, cod):

    fechas_peluqueria = fecha.objects.all()
    
    return render(request, "seleccionar_fecha.html",{ 
        'fechas_peluqueria':fechas_peluqueria,
        'cod':cod
    })
    






def confirmar_hora (request, cod, cod2):


    horario = horas_peluqueria.objects.all()

    return render(request, "confirmar_hora.html",{ 
        'cod2':cod2,
        'cod':cod,
        'horario':horario
    })
    

def hora_confirmada (request, cod, cod2):


    cod2 = cod2 + 1
    hora_peluquero = peluquero_horas.objects.get(pk = cod)
    hora = horas_peluqueria.objects.get(pk = cod2)
    hora_peluquero.id_horas_h = horas_peluqueria.objects.get(pk = cod2)
    hora_peluquero.save()

    return redirect ('/')






def reservarHora (request):

    return redirect( '/' )



