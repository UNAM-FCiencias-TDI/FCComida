# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0007_auto_20151214_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comercio',
            name='comedor',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='facultad',
            field=models.CharField(default=b'', max_length=50, choices=[(b'Facultad de Arquitectura', b'Facultad de Arquitectura'), (b'Facultad de Derecho', b'Facultad de Derecho'), (b'Facultad de Ciencias', b'Facultad de Ciencias'), (b'Facultad de Ciencias Politicas y Sociales', b'Facultad de Ciencias Politicas y Sociales'), (b'Facultad de Contaduria y Administracion', b'Facultad de Contaduria y Administracion'), (b'Facultad de Economia', b'Facultad de Economia'), (b'Facultad de Filosofia y Letras', b'Facultad de Filosofia y Letras'), (b'Facultad de Ingenieria', b'Facultad de Ingenieria'), (b'Facultad de Medicina', b'Facultad de Medicina'), (b'Facultad de Quimica', b'Facultad de Quimica'), (b'Facultad de Odontologia', b'Facultad de Odontologia'), (b'Facultad de Psicologia', b'Facultad de Psicologia'), (b'Facultad de Veterinaria y Zootecnia', b'Facultad de Veterinaria y Zootecnia')]),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='foto',
            field=models.ImageField(upload_to=b'comercio_img/', blank=True),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='mayor_precio',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.5)]),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='menor_precio',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.5)]),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='nombre',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
