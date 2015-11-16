# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Califica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('califica', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('comercioId', models.ForeignKey(to='comercio.Comercio')),
                ('usuarioId', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comentario', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('comercioId', models.ForeignKey(to='comercio.Comercio')),
                ('usuarioId', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
