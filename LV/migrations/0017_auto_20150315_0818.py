# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LV', '0016_auto_20150315_0814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='info_title',
            new_name='title',
        ),
    ]
