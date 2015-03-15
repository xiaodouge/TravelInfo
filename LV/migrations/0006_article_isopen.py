# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LV', '0005_auto_20150314_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='isopen',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
