# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LV', '0020_auto_20150503_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
    ]
