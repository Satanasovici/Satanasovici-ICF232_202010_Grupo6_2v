# Generated by Django 3.0.6 on 2020-11-12 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peluqueria', '0006_auto_20201112_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fecha',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha'),
        ),
    ]
