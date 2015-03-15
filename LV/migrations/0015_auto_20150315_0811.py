# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LV', '0014_auto_20150315_0714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='isopen',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
    ]
