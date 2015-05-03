# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LV', '0019_remove_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date_time',
            field=models.CharField(max_length=50, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', blank=True),
            preserve_default=True,
        ),
    ]
