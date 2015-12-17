# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0009_auto_20151214_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comercio',
            name='latitud',
            field=models.DecimalField(default=19.3234728, max_digits=30, decimal_places=15, validators=[django.core.validators.MaxValueValidator(90.0), django.core.validators.MinValueValidator(-90.0)]),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='longitud',
            field=models.DecimalField(default=-99.1814817, max_digits=30, decimal_places=15, validators=[django.core.validators.MaxValueValidator(180.0), django.core.validators.MinValueValidator(-180.0)]),
        ),
    ]
