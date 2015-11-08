# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('idCalificacion', models.IntegerField(serialize=False, primary_key=True)),
                ('calificacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('idComentario', models.IntegerField(serialize=False, primary_key=True)),
                ('comentario', models.TextField()),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Comercio',
            fields=[
                ('idComercio', models.IntegerField(serialize=False, primary_key=True)),
                ('calif', models.IntegerField()),
                ('comedor', models.BinaryField()),
                ('facultad', models.CharField(max_length=200)),
                ('foto', models.ImageField(upload_to=b'')),
                ('latitud', models.IntegerField()),
                ('longitud', models.IntegerField()),
                ('mayorPrecio', models.FloatField()),
                ('menorPrecio', models.FloatField()),
                ('nombre', models.CharField(max_length=100)),
                ('recomendadaId', models.IntegerField()),
                ('descripcion', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('idComida', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('tipo', models.CharField(max_length=200)),
                ('comercioId', models.ForeignKey(to='usuarios.Comercio')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.IntegerField(serialize=False, primary_key=True)),
                ('apellidoP', models.CharField(max_length=100)),
                ('apellidoM', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('contrasenia', models.CharField(max_length=300)),
                ('correo', models.EmailField(max_length=100)),
                ('nombreUsuario', models.CharField(max_length=100)),
                ('clss', models.BinaryField()),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='comercioId',
            field=models.ForeignKey(to='usuarios.Comercio'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuarioId',
            field=models.ForeignKey(to='usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='comercioId',
            field=models.ForeignKey(to='usuarios.Comercio'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='usuarioId',
            field=models.ForeignKey(to='usuarios.Usuario'),
        ),
    ]
