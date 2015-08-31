# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20150827_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumb_url',
            field=models.ImageField(verbose_name=django.core.files.storage.FileSystemStorage(location='/media/projects'), upload_to=''),
        ),
    ]
