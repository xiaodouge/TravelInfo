# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LV', '0006_article_isopen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=50, blank=True)),
                ('address', models.CharField(max_length=50, blank=True)),
                ('tick', models.CharField(max_length=50, blank=True)),
                ('open_time', models.CharField(max_length=50, blank=True)),
                ('category', models.CharField(max_length=50, blank=True)),
                ('isopen', models.CharField(max_length=50, blank=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['-date_time'],
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
