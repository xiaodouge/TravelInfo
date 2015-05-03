# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LV', '0017_auto_20150315_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='articles',
            name='address',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articles',
            name='city',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=models.TextField(null=True, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articles',
            name='country',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\x9b\xbd\xe5\xae\xb6', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articles',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articles',
            name='headImg',
            field=models.FileField(upload_to=b'upload/', verbose_name=b'\xe6\x8f\x92\xe5\x9b\xbe', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articles',
            name='open_time',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xbc\x80\xe6\x94\xbe\xe6\x97\xb6\xe9\x97\xb4', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articles',
            name='tick',
            field=models.CharField(max_length=50, verbose_name=b'\xe7\xa5\xa8\xe4\xbb\xb7', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98', blank=True),
            preserve_default=True,
        ),
    ]
