# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('apellidoP', models.CharField(max_length=100)),
                ('apellidoM', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('contrasenia', models.CharField(max_length=300)),
                ('correo', models.EmailField(max_length=100)),
                ('nombreUsuario', models.CharField(max_length=100)),
                ('clss', models.BooleanField()),
            ],
        ),
    ]
