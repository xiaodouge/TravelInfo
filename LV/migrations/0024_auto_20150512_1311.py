# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LV', '0023_auto_20150512_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='pubuser',
            field=models.CharField(default=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98', max_length=50, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe8\x80\x85'),
            preserve_default=True,
        ),
    ]
