# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calificacion',
            name='comercioId',
        ),
        migrations.RemoveField(
            model_name='calificacion',
            name='usuarioId',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='comercioId',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='usuarioId',
        ),
        migrations.RemoveField(
            model_name='comida',
            name='comercioId',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='idUsuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='clss',
            field=models.BooleanField(),
        ),
        migrations.DeleteModel(
            name='Calificacion',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.DeleteModel(
            name='Comercio',
        ),
        migrations.DeleteModel(
            name='Comida',
        ),
    ]
