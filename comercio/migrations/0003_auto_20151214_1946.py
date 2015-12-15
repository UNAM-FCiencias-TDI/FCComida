# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0002_auto_20151214_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='comercio',
            name='descripcion',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='comercio',
            name='url',
            field=models.CharField(default=b'', max_length=101),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='facultad',
            field=models.CharField(max_length=50, choices=[(b'Facultad de Arquitectura', b'Facultad de Arquitectura'), (b'Facultad de Derecho', b'Facultad de Derecho'), (b'Facultad de Ciencias', b'Facultad de Ciencias'), (b'Facultad de Ciencias Politicas y Sociales', b'Facultad de Ciencias Politicas y Sociales'), (b'Facultad de Contaduria y Administracion', b'Facultad de Contaduria y Administracion'), (b'Facultad de Economia', b'Facultad de Economia'), (b'Facultad de Filosofia y Letras', b'Facultad de Filosofia y Letras'), (b'Facultad de Ingenieria', b'Facultad de Ingenieria'), (b'Facultad de Medicina', b'Facultad de Medicina'), (b'Facultad de Quimica', b'Facultad de Quimica'), (b'Facultad de Odontologia', b'Facultad de Odontologia'), (b'Facultad de Psicologia', b'Facultad de Psicologia'), (b'Facultad de Veterinaria y Zootecnia', b'Facultad de Veterinaria y Zootecnia')]),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
