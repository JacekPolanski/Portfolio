# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150827_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='profession',
            field=models.CharField(max_length=100, default='programista'),
            preserve_default=False,
        ),
    ]
