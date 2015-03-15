# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LV', '0011_auto_20150314_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
