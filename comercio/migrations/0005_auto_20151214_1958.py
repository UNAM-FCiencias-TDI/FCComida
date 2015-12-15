# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0004_auto_20151214_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comercio',
            name='calificacion',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
