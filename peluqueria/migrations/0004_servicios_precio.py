# Generated by Django 3.0.10 on 2020-11-02 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peluqueria', '0003_auto_20201102_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicios',
            name='precio',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
