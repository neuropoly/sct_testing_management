# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-26 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0010_auto_20180326_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acquisition',
            name='center',
            field=models.CharField(default='None', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='session',
            field=models.CharField(default='None', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='study',
            field=models.CharField(default='None', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='acquisition',
            unique_together=set([('center', 'study', 'session')]),
        ),
    ]
