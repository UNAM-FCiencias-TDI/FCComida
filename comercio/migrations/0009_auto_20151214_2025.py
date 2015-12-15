# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0008_auto_20151214_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comercio',
            name='mayor_precio',
            field=models.FloatField(default=0.5, validators=[django.core.validators.MinValueValidator(0.5)]),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='menor_precio',
            field=models.FloatField(default=0.5, validators=[django.core.validators.MinValueValidator(0.5)]),
        ),
    ]
