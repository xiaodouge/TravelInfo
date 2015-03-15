# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LV', '0010_auto_20150314_1041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='info_title',
        ),
    ]
