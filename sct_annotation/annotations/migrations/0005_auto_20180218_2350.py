# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-19 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0004_auto_20180218_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='contrast_category',
            field=models.CharField(max_length=32),
        ),
    ]