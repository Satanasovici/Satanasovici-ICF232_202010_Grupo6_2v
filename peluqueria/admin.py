from django.contrib import admin
from .models import peluqueros, servicios, peluqueros_servicios, cliente, estado_hora, estado_reserva, horas_peluqueria, peluquero_horas, reserva, fecha

admin.site.register(servicios)
admin.site.register(peluqueros)
#admin.site.register(horario_peluquero)
admin.site.register(peluqueros_servicios)
admin.site.register(cliente)
admin.site.register(estado_hora)
admin.site.register(estado_reserva)
admin.site.register(horas_peluqueria)
admin.site.register(fecha)
admin.site.register(peluquero_horas)
admin.site.register(reserva)