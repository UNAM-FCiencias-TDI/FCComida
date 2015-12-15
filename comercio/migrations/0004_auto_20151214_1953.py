# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0003_auto_20151214_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comercio',
            name='url',
        ),
        migrations.AddField(
            model_name='comercio',
            name='clave',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
