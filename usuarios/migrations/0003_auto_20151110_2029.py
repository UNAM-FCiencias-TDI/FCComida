# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20151110_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuarioid',
            field=models.IntegerField(default=datetime.datetime(2015, 11, 11, 2, 29, 11, 48981, tzinfo=utc), serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
