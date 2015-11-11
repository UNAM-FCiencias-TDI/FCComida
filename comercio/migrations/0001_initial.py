# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comercio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calificacion', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('comedor', models.BooleanField()),
                ('facultad', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.BinaryField()),
                ('latitud', models.DecimalField(max_digits=5, decimal_places=3, validators=[django.core.validators.MaxValueValidator(90.0), django.core.validators.MinValueValidator(-90.0)])),
                ('longitud', models.DecimalField(max_digits=5, decimal_places=3, validators=[django.core.validators.MaxValueValidator(180.0), django.core.validators.MinValueValidator(-180.0)])),
                ('mayor_precio', models.FloatField(validators=[django.core.validators.MinValueValidator(0.5)])),
                ('menor_precio', models.FloatField(validators=[django.core.validators.MinValueValidator(0.5)])),
            ],
        ),
    ]
