# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-17 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0012_auto_20180403_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='resolution',
        ),
        migrations.AddField(
            model_name='image',
            name='axial',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='image',
            name='corrinal',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='image',
            name='is_isotropic',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='image',
            name='sagittal',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='image',
            name='filename',
            field=models.CharField(help_text='path prefix: /Volumes/sct_testing/large/', max_length=512, unique=True, verbose_name='File path'),
        ),
        migrations.AlterField(
            model_name='labeledimage',
            name='filename',
            field=models.CharField(help_text='path prefix: /Volumes/sct_testing/large/', max_length=512, unique=True, verbose_name='File path'),
        ),
    ]
