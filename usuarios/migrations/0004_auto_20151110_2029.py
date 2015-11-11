# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20151110_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='usuarioid',
        ),
        migrations.AddField(
            model_name='usuario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=datetime.datetime(2015, 11, 11, 2, 29, 54, 823860, tzinfo=utc), serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
