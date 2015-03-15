# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('LV', '0012_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='headImg',
            field=models.FileField(default=datetime.datetime(2015, 3, 15, 6, 56, 34, 569887, tzinfo=utc), upload_to=b'./upload/'),
            preserve_default=False,
        ),
    ]
