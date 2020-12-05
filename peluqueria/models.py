from django.db import models
from django.contrib.auth.models import User



class Peluquero_info(models.Model):
   
    nombre = models.CharField(max_length = 15)
    apellido = models.CharField(max_length = 20)
    rubro = models.CharField(max_length = 20)
    telefono = models.CharField(max_length = 9)
    email = models.EmailField()
    horario = models.CharField(max_length = 30)


# Create your models here.



#######################################################################################################################




class cliente (models.Model):

    id_usuario_c = models.ForeignKey(User, on_delete=models.CASCADE)
    rut_cliente = models.CharField(max_length=9,primary_key=True)
    edad = models.IntegerField()




class peluqueros (models.Model):

    rut_usuario = models.IntegerField(primary_key=True)
    edad = models.IntegerField()
#   id_horario_p = models.ForeignKey(horario_peluquero, on_delete=models.CASCADE)
    id_usuario_p = models.ForeignKey(User, on_delete=models.CASCADE)
    



class servicios (models.Model):

    id_servicios = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    duracion_aproximada = models.CharField(max_length=20)
    precio_servicio = models.IntegerField()




class peluqueros_servicios (models.Model):

    rut_usuario_p = models.ForeignKey(peluqueros, on_delete=models.CASCADE)
    id_servicios_p = models.ForeignKey(servicios, on_delete=models.CASCADE)


class estado_hora (models.Model):

    if_estado_hora = models.IntegerField(primary_key=True)
    estado = models.BooleanField()



class horas_peluqueria (models.Model):

    id_hora = models.IntegerField(primary_key=True)
    hora_inicio = models.CharField(max_length=10)
    id_estado = models.ForeignKey(estado_hora, on_delete=models.CASCADE)



class fecha(models.Model):

    id_fecha = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha')



class peluquero_horas (models.Model):

    id_peluquero_h = models.ForeignKey(peluqueros,on_delete=models.CASCADE)
    id_horas_h = models.ForeignKey (horas_peluqueria, on_delete=models.CASCADE)
    id_fecha_h = models.ForeignKey(fecha, on_delete=models.CASCADE)



class estado_reserva (models.Model):
    id_estado_reserva = models.IntegerField(primary_key=True)
    estado = models.BooleanField()


class reserva (models.Model):

    id_reserva_r = models.AutoField(primary_key=True)
    id_cliente_r = models.ForeignKey(cliente,on_delete=models.CASCADE)
    id_estado_r = models.ForeignKey(estado_reserva, on_delete=models.CASCADE)
    id_hora_r = models.ForeignKey(horas_peluqueria, on_delete=models.CASCADE)
    id_servicio_r = models.ForeignKey(servicios, on_delete=models.CASCADE)
    id_fecha_r = models.ForeignKey(fecha, on_delete=models.CASCADE)
    id_peluquero_r = models.ForeignKey(peluqueros, on_delete=models.CASCADE)



    




