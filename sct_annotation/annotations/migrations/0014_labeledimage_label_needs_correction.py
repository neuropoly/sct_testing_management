# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-30 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0013_auto_20180417_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='labeledimage',
            name='label_needs_correction',
            field=models.BooleanField(default=False),
        ),
    ]