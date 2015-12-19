# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0002_auto_20151214_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='facultad',
            field=models.CharField(max_length=200, choices=[(b'Facultad de Arquitectura', b'Facultad de Arquitectura'), (b'Facultad de Derecho', b'Facultad de Derecho'), (b'Facultad de Ciencias', b'Facultad de Ciencias'), (b'Facultad de Ciencias Politicas y Sociales', b'Facultad de Ciencias Pol\xc3\xadticas y Sociales'), (b'Facultad de Contaduria y Administracion', b'Facultad de Contadur\xc3\xada y Administraci\xc3\xb3n'), (b'Facultad de Economia', b'Facultad de Econom\xc3\xada'), (b'Facultad de Filosofia y Letras', b'Facultad de Filosof\xc3\xada y Letras'), (b'Facultad de Ingenieria', b'Facultad de Ingenier\xc3\xada'), (b'Facultad de Medicina', b'Facultad de Medicina'), (b'Facultad de Quimica', b'Facultad de Qu\xc3\xadmica'), (b'Facultad de Odontologia', b'Facultad de Odontolog\xc3\xada'), (b'Facultad de Psicologia', b'Facultad de Psicolog\xc3\xada'), (b'Facultad de Veterinaria y Zootecnia', b'Facultad de Veterinaria y Zootecnia')]),
        ),
    ]
