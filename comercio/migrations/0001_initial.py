# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comercio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(default=b'', max_length=50)),
                ('facultad', models.CharField(default=b'', max_length=50, choices=[(b'Facultad de Arquitectura', b'Facultad de Arquitectura'), (b'Facultad de Derecho', b'Facultad de Derecho'), (b'Facultad de Ciencias', b'Facultad de Ciencias'), (b'Facultad de Ciencias Politicas y Sociales', b'Facultad de Ciencias Politicas y Sociales'), (b'Facultad de Contaduria y Administracion', b'Facultad de Contaduria y Administracion'), (b'Facultad de Economia', b'Facultad de Economia'), (b'Facultad de Filosofia y Letras', b'Facultad de Filosofia y Letras'), (b'Facultad de Ingenieria', b'Facultad de Ingenieria'), (b'Facultad de Medicina', b'Facultad de Medicina'), (b'Facultad de Quimica', b'Facultad de Quimica'), (b'Facultad de Odontologia', b'Facultad de Odontologia'), (b'Facultad de Psicologia', b'Facultad de Psicologia'), (b'Facultad de Veterinaria y Zootecnia', b'Facultad de Veterinaria y Zootecnia')])),
                ('calificacion', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('comedor', models.BooleanField(default=True)),
                ('foto', models.ImageField(upload_to=b'comercio_img/', blank=True)),
                ('latitud', models.DecimalField(default=19.3234728, max_digits=30, decimal_places=15, validators=[django.core.validators.MaxValueValidator(90.0), django.core.validators.MinValueValidator(-90.0)])),
                ('longitud', models.DecimalField(default=-99.1814817, max_digits=30, decimal_places=15, validators=[django.core.validators.MaxValueValidator(180.0), django.core.validators.MinValueValidator(-180.0)])),
                ('mayor_precio', models.FloatField(default=0.5, validators=[django.core.validators.MinValueValidator(0.5)])),
                ('menor_precio', models.FloatField(default=0.5, validators=[django.core.validators.MinValueValidator(0.5)])),
                ('descripcion', models.CharField(default=b'', max_length=200)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
