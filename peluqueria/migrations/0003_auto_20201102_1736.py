# Generated by Django 3.0.10 on 2020-11-02 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peluqueria', '0002_cliente_estado_hora_estado_reserva_fecha_horas_peluqueria_peluquero_horas_peluqueros_peluqueros_serv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peluqueros',
            name='rut_usuario',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
