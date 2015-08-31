# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20150831_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='thumb_url',
            new_name='thumb',
        ),
    ]
