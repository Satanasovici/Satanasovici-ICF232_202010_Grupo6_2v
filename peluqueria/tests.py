from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.test import Client
from rest_framework import status
from django.urls import path
from datetime import date
from datetime import datetime
from datetime import time

# Create your tests here.

class usuariotestcase(TestCase):
    def setUp(self):
        self.username = "Cliente"
        self.first_name = "User"
        self.last_name = "Prueba"
        self.email = "cliente01@gmail.com"
        self.usuario_c = User(username=self.username,first_name=self.username,last_name=self.last_name,email=self.email)
        self.username = "Peluquero"
        self.first_name = "User"
        self.last_name = "Prueba"
        self.email = "peluquero01@gmail.com"
        self.usuario_p = User(username=self.username,first_name=self.first_name,last_name=self.last_name,email=self.email)

    def test_creacion_de_usuarios(self):
        """Test de creación de usuarios"""

        self.username = "Cliente"
        self.first_name = "User"
        self.last_name = "Prueba"
        self.email = "cliente01@gmail.com"
        self.rut_usuario = 194568789
        self.edad_usuario = 25

        self.user=User.objects.create_superuser('servidor', 'api@test.com', "Secret.123")
        
        User.objects.create(
            first_name = "User",
            username = "Cliente",
            last_name = "Prueba",
            email = "cliente01@gmail.com"
        )     

        User.objects.create(
            first_name = "User",
            username = "Peluquero",
            last_name = "Prueba",
            email = "Peluquero01@gmail.com"
        ) 

        cliente.objects.create(
            id_usuario_c = User.objects.get(pk = 1),
            rut_cliente = 194568789,
            edad = 25
        )

        peluqueros.objects.create(
            id_usuario_p = User.objects.get(pk = 2),
            rut_usuario = 194564568,
            edad = 35
        )

class serviciostestcase(TestCase):
    def setUp(self):
        self.nombre = "corte niño"
        self.duracion = "30 minutos"
        self.precio = 8000
        self.servicio = servicios(nombre=self.nombre,duracion_aproximada=self.duracion,precio_servicio=self.precio)
 

    def test_creacion_de_servicios(self):
        """Test de creación de servicio"""

        User.objects.create(
            first_name = "User",
            username = "Peluquero",
            last_name = "Prueba",
            email = "Peluquero01@gmail.com"
        ) 

    def test_creacion_de_horas(self):
        """Test de creación de horas de la peluqueria"""
        estado_hora.objects.create(
            estado = 1,
            if_estado_hora = 1
        )

        horas_peluqueria.objects.create(
            id_hora = 1,
            hora_inicio = "10:30",
            id_estado = estado_hora.objects.get(if_estado_hora=1)
        )

    def test_creacion_de_servicios_horas(self):
        """Test de creación de servicios"""

        User.objects.create(
            first_name = "User",
            username = "Peluquero",
            last_name = "Prueba",
            email = "Peluquero01@gmail.com"
        ) 

        peluqueros.objects.create(
            id_usuario_p = User.objects.get(pk = 1),
            rut_usuario = 194564568,
            edad = 35
        )
        servicios.objects.create(
            nombre = "corte niño",
            duracion_aproximada = "30 minutos",
            precio_servicio = 8000
        )

        peluqueros_servicios.objects.create(
            rut_usuario_p = peluqueros.objects.get(rut_usuario = 194564568),
            id_servicios_p = servicios.objects.get(pk = 1)
        )

class fechatestcase(TestCase):
    def test_creacion_de_servicios_horas(self):
        """Test de creación de fechas"""

        fecha.objects.create(
            fecha = date.today()
        )

class horaspeluquerostestcase(TestCase):
    def test_creacion_de_horas_peluquero(self):
        """Test de creación de horas del peluquero"""
        User.objects.create(
                first_name = "User",
                username = "Peluquero",
                last_name = "Prueba",
                email = "Peluquero01@gmail.com"
            ) 

        peluqueros.objects.create(
            id_usuario_p = User.objects.get(pk = 1),
            rut_usuario = 194564568,
            edad = 35
        )

        fecha.objects.create(
            fecha = date.today()
        )

        estado_hora.objects.create(
            estado = 1,
            if_estado_hora = 1
        )

        horas_peluqueria.objects.create(
            id_hora = 1,
            hora_inicio = "10:30",
            id_estado = estado_hora.objects.get(if_estado_hora=1)
        )

        peluquero_horas.objects.create(
            id_fecha_h = fecha.objects.get(fecha = date.today()),
            id_peluquero_h = peluqueros.objects.get(rut_usuario = 194564568),
            id_horas_h = horas_peluqueria.objects.get(id_hora=1)

        )

class reservatestcase(TestCase):
    def test_creacion_de_reservas(self):
        """Test de creación de horas del peluquero"""
        User.objects.create(
                first_name = "User",
                username = "Peluquero",
                last_name = "Prueba",
                email = "Peluquero01@gmail.com"
            ) 
        User.objects.create(
            first_name = "User",
            username = "Cliente",
            last_name = "Prueba",
            email = "cliente01@gmail.com"
        )

        cliente.objects.create(
            id_usuario_c = User.objects.get(pk = 2),
            rut_cliente = 194568789,
            edad = 25
        )  

        peluqueros.objects.create(
            id_usuario_p = User.objects.get(pk = 1),
            rut_usuario = 194564568,
            edad = 35
        )

        fecha.objects.create(
            fecha = date.today()
        )

        estado_hora.objects.create(
            estado = 1,
            if_estado_hora = 1
        )

        horas_peluqueria.objects.create(
            id_hora = 1,
            hora_inicio = "10:30",
            id_estado = estado_hora.objects.get(if_estado_hora=1)
        )

        peluquero_horas.objects.create(
            id_fecha_h = fecha.objects.get(fecha = date.today()),
            id_peluquero_h = peluqueros.objects.get(rut_usuario = 194564568),
            id_horas_h = horas_peluqueria.objects.get(id_hora=1)
        )
        estado_reserva.objects.create (
            estado = 1,
            id_estado_reserva = 1
        )

        servicios.objects.create(
            nombre = "corte niño",
            duracion_aproximada = "30 minutos",
            precio_servicio = 8000
        )

        reserva.objects.create(
            id_cliente_r = cliente.objects.get(rut_cliente = 194568789),
            id_estado_r = estado_reserva.objects.get(id_estado_reserva=1),
            id_hora_r = horas_peluqueria.objects.get(id_hora=1),
            id_servicio_r = servicios.objects.get(pk=1),
            id_fecha_r = fecha.objects.get(fecha = date.today()),
            id_peluquero_r = peluqueros.objects.get(rut_usuario = 194564568)
        )

        
        




    



