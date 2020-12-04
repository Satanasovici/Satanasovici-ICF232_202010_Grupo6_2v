"""digitalizacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from peluqueria.views import quienes_somos, catalogo, perfil, informacion_peluqueria, agenda, index_prueba, Cortes, contacto, profesionales, Alisados, Tintes, Lavados, Peinados, Afeitados , Editar_Perfil, seleccionar_peluquero, seleccionar_hora, confirmar_hora, hora_confirmada, seleccionar_fecha, peluquero_horas, poblar_fechas, poblar_horas, ver_reservas, pago_paypal,total_reservas, ver_total_reservas, usuarios_clientes,fechas_peluquero, ver_reservas_peluquero, ver_reservas_hoy

from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_prueba),
    #path('loginEmpleado', views.loginEmpleado),
    path('loginCliente', views.loginCliente),
    path('registro', views.register),
    path('index', views.index_cliente),
    path('logout', views.logout),
    path('catalogo', catalogo),
    path('agenda', agenda),
    path('perfil', perfil),
    path('configuracion', views.config),
    path('delete', views.deleteuser),
    path('informacion_peluqueria', informacion_peluqueria),
    path('modif', views.editProfile),
    path('password', views.changePassword),
    path('prueba', index_prueba),
    path('Cortes', Cortes),
    path('Tintes', Tintes),
    path('Lavados', Lavados),
    path('Alisados', Alisados),
    path('Afeitado', Afeitados),
    path('Peinados', Peinados),
    path('Contacto', contacto),
    path('Profesionales', profesionales),
    path('quienes_somos', quienes_somos),
    path('Editar', Editar_Perfil),
    path('selectPeluquero/<int:cod>', seleccionar_peluquero),
    path('selectHora/<int:cod2>/<int:cod>/<int:cod3>', seleccionar_hora),
    path('confirmHora/<int:cod>/<int:cod2>/<int:cod3>', confirmar_hora),
    path('hora_confirmada/<int:cod>/<int:cod2>/<int:cod3>',hora_confirmada),
    path('seleccionar_fecha/<int:cod>/<int:cod2>',seleccionar_fecha),
    path('poblar',poblar_horas),
    path('fechas',poblar_fechas),
    path('reservas',ver_reservas),
    path('pago',pago_paypal),
    path('total_reservas',total_reservas),
    path('ver_total_reservas/<int:cod>',ver_total_reservas),
    path('Clientes',usuarios_clientes),
    path('fechas_peluquero', fechas_peluquero),
    path('ver_reservas_peluquero/<int:cod>',ver_reservas_peluquero),
    path('ver_reservas_hoy',ver_reservas_hoy),


    path('Login',views.login),
]
