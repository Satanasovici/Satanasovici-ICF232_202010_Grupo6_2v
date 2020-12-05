from .models import fecha
from .models import peluquero_horas
from .models import horas_peluqueria
from .models import peluqueros
from datetime import timedelta


def poblar_fechas():

    for dia in fecha:
        for hora in horas_peluqueria:
            if hora % 2 != 0:
                for peluquero in peluqueros:
                    peluquero_horas.objects.create(
                        id_peluquero_h = peluquero,
                        id_horas_h = hora,
                        id_fecha = dia
                    )
