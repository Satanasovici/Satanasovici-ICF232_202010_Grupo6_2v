from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as do_logout
from .models import Peluquero_info, servicios, peluqueros, peluqueros_servicios, peluquero_horas, horas_peluqueria, fecha, reserva, cliente, estado_reserva
from datetime import date
from datetime import datetime
from datetime import time
from django.utils import timezone, dateformat
from django.db.models import Count
from django.http import JsonResponse
from django.contrib.auth.models import User
from datetime import timedelta
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
    

def profesionales(request):
    personas = peluqueros.objects.all()
    usuario = User.objects.all()
  
    return render(request, "pagina_profesionales.html",{
        'personas':personas,
        'usuario':usuario
    })



def seleccionar_peluquero (request, cod):

    peluquero = peluqueros_servicios.objects.all()
    nombre = User.objects.all()
    usuarios = peluqueros.objects.all()

    return render (request, "seleccionar_peluquero.html", {
        'peluqueros':peluquero,
        'cod':cod,
        'nombre':nombre,
        'usuarios':usuarios
        
    })


def seleccionar_hora (request,cod,cod2,cod3):

    

   
    horas = peluquero_horas.objects.all()
    horario = horas_peluqueria.objects.all()
    disponible = datetime.now().strftime('%H:%M')
    hoy = date.today()
    fechas = fecha.objects.all()    

    return render (request, "ver_horas.html", {
        'horas':horas,
        'cod':cod,
        'cod2':cod2,
        'cod3':cod3,
        'horario':horario,
        'disponible':disponible,
        'hoy':hoy,
        'fechas':fechas
    })




def seleccionar_fecha (request, cod, cod2):

    fechas_peluqueria = fecha.objects.all()
    
    hoy = date.today()
    
    #x = datetime.now().strftime('%H:%M')
    #return HttpResponse(x)
    return render(request, "seleccionar_fecha.html",{ 
        'fechas_peluqueria':fechas_peluqueria,
        'cod':cod,
        'cod2':cod2,
        'hoy':hoy
    })





def confirmar_hora (request, cod, cod2, cod3):


    horario = horas_peluqueria.objects.all()

    dato_precio = servicios.objects.get(pk=cod3)
    precio = dato_precio.precio_servicio
    dolar = precio/765
    dolar = int(dolar)
    #return HttpResponse (dolar)

    return render(request, "confirmar_hora.html",{ 
        'cod2':cod2,
        'cod':cod,
        'cod3':cod3,
        'horario':horario,
        'dolar':dolar
    })
    

def hora_confirmada (request, cod, cod2, cod3 ):


    cod2 = cod2 + 1
    hora_peluquero = peluquero_horas.objects.get(pk = cod)
    hora = horas_peluqueria.objects.get(pk = cod2)
    hora_peluquero.id_horas_h = horas_peluqueria.objects.get(pk = cod2)
    Usuario = request.user.id
    clientes = cliente.objects.get(id_usuario_c = Usuario)
    hora_peluquero.save()

    reserva.objects.create(

        id_cliente_r = cliente.objects.get(id_usuario_c = Usuario),
        id_estado_r = estado_reserva.objects.get(id_estado_reserva = 1),
        id_hora_r = horas_peluqueria.objects.get(pk = cod2),
        id_servicio_r = servicios.objects.get(pk = cod3),
        id_fecha_r = hora_peluquero.id_fecha_h,
        id_peluquero_r = hora_peluquero.id_peluquero_h 
    )

    return redirect ( '/' )






def reservarHora (request):

    return redirect( '/' )



def poblar_horas(request):

    horario = horas_peluqueria.objects.all()
    fecha_p = fecha.objects.all()
    peluquero = peluqueros.objects.all()
    hora_peluquero = peluquero_horas.objects.all()
    cantidad_peluqueros = 0
    cantidad_fechas = 0
    cantidad = 0
    respuesta = 0
    acum = 0

    for dia in fecha_p:
        

        for fechass in hora_peluquero:
            if dia.id_fecha == fechass.id_fecha_h_id:
                respuesta = respuesta + 1
            else:
                respuesta = respuesta + respuesta
        if respuesta == 0:
            #respuesta2 = fecha_id.id_fecha_h
            for hora in horario:
                if hora.id_hora % 2 != 0:
                    for peluquero_p in peluquero:
                        peluquero_horas.objects.create(
                            id_peluquero_h = peluqueros.objects.get(pk=peluquero_p.rut_usuario),
                            id_horas_h = horas_peluqueria.objects.get(pk=hora.id_hora),
                            id_fecha_h = fecha.objects.get(pk=dia.id_fecha)
                        )
                            #       cantidad = 0
                            #peluquero_horas.save()
        else:
            respuesta = 0
    return HttpResponse( "Listo" )
                




def poblar_fechas(request):

    fecha_p = fecha.objects.all()
    
    for fechas in fecha_p:
        f = fechas.fecha
    fecha.objects.create(
        fecha = f + timedelta(days = 1)
    )

    return HttpResponse("Completado")



def ver_reservas(request):

    datos = reserva.objects.all()
    Usuario = request.user.id
    clientes = cliente.objects.get(id_usuario_c = Usuario)
    fechas = fecha.objects.all()
    peluquero = peluqueros.objects.all()
    horas = horas_peluqueria.objects.all()
    servicio = servicios.objects.all()
    nombre = User.objects.all()

   # datos_reserva = reserva.objects.get(id_cliente_r = clientes)
    

    return render(request, "ver_reservas.html",{ 
        'datos':datos,
        'clientes':clientes,
        'fechas':fechas,
        'peluquero':peluquero,
        'horas':horas,
        'servicio':servicio,
        'nombre':nombre
    })

    

def seleccionar_fecha (request, cod, cod2):

    fechas_peluqueria = fecha.objects.all()
    
    hoy = date.today()
    
    return render(request, "seleccionar_fecha.html",{ 
        'fechas_peluqueria':fechas_peluqueria,
        'cod':cod,
        'cod2':cod2,
        'hoy':hoy
    })




def total_reservas(request):

    reservas = reserva.objects.all()
    fechas_peluqueria = fecha.objects.all()

    return render(request,"total_reservas.html",{
        'reservas':reservas,
        'fechas_peluqueria':fechas_peluqueria,
        
    })


def ver_total_reservas(request, cod):


    reservas = reserva.objects.all()



    datos = reserva.objects.all()
    clientes = cliente.objects.all()
    fechas = fecha.objects.all()
    peluquero = peluqueros.objects.all()
    horas = horas_peluqueria.objects.all()
    servicio = servicios.objects.all()
    nombre = User.objects.all()






    return render(request,"ver_total_reservas.html",{
        'cod':cod,
        'datos':datos,
        'clientes':clientes,
        'fechas':fechas,
        'peluquero':peluquero,
        'horas':horas,
        'servicio':servicio,
        'nombre':nombre
    })





def pago_paypal(request):

    return render(request, "paypal.html")


