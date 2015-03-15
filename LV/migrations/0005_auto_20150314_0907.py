# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LV', '0004_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='address',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='city',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='country',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='open_time',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='tick',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
