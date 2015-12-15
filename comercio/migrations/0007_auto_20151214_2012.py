# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0006_auto_20151214_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comercio',
            name='calificacion',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='latitud',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=3, validators=[django.core.validators.MaxValueValidator(90.0), django.core.validators.MinValueValidator(-90.0)]),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='longitud',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=3, validators=[django.core.validators.MaxValueValidator(180.0), django.core.validators.MinValueValidator(-180.0)]),
        ),
    ]
