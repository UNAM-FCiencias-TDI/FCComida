# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='facultad',
            field=models.CharField(max_length=200, choices=[(b'Facultad de Arquitectura', b'Facultad de Arquitectura'), (b'Facultad de Derecho', b'Facultad de Derecho'), (b'Facultad de Ciencias', b'Facultad de Ciencias'), (b'Facultad de Ciencias Pol\xc3\xadticas y Sociales', b'Facultad de Ciencias Pol\xc3\xadticas y Sociales'), (b'Facultad de Contadur\xc3\xada y Administraci\xc3\xb3n', b'Facultad de Contadur\xc3\xada y Administraci\xc3\xb3n'), (b'Facultad de Econom\xc3\xada', b'Facultad de Econom\xc3\xada'), (b'Facultad de Filosof\xc3\xada y Letras', b'Facultad de Filosof\xc3\xada y Letras'), (b'Facultad de Ingenier\xc3\xada', b'Facultad de Ingenier\xc3\xada'), (b'Facultad de Medicina', b'Facultad de Medicina'), (b'Facultad de Qu\xc3\xadmica', b'Facultad de Qu\xc3\xadmica'), (b'Facultad de Odontolog\xc3\xada', b'Facultad de Odontolog\xc3\xada'), (b'Facultad de Psicolog\xc3\xada', b'Facultad de Psicolog\xc3\xada'), (b'Facultad de Veterinaria y Zootecnia', b'Facultad de Veterinaria y Zootecnia')]),
        ),
    ]
