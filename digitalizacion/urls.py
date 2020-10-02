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
from peluqueria.views import catalogo, perfil, informacion_peluqueria, agenda, index_prueba, Cortes, contacto, profesionales
from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),
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
    #path('BorrarCuenta', views.opcionesCuenta),
    path('modif', views.editProfile),
    path('password', views.changePassword),
    path('prueba', index_prueba),
    path('Cortes', Cortes),
    #path('Tintes', tintes),
    #path('Lavados', lavados),
    #path('Alisados', alisados),
    #path('Afeitado', afeitado),
    #path('Peinados', peinados),
    path('Contacto', contacto),
    path('Profesionales', profesionales),
    #path('Quienes_somos', quienes_somos),
    #path('Direccion', direccion),
    #path('Servicios', servicios),
    


    path('Login',views.login),
]
