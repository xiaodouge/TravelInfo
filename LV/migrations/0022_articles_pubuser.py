# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LV', '0021_auto_20150503_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='pubuser',
            field=models.CharField(default=b'root', verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe8\x80\x85', max_length=50, editable=False),
            preserve_default=True,
        ),
    ]
