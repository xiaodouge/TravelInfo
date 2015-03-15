# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LV', '0013_article_headimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='headImg',
            field=models.FileField(upload_to=b'./upload/', blank=True),
            preserve_default=True,
        ),
    ]
