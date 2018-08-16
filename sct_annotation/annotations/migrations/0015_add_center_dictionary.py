# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-16 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0014_labeledimage_label_needs_correction'),
    ]

    operations = [
        migrations.CreateModel(
            name='CenterDictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_acronym', models.CharField(max_length=32, unique=True)),
                ('center_name', models.CharField(max_length=32)),
                ('center_city', models.CharField(max_length=32)),
                ('center_country', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': 'Center Dictionary',
            },
        ),
        migrations.AddField(
            model_name='acquisition',
            name='center_link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='annotations.CenterDictionary'),
        ),
    ]
