# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-16 17:39
from __future__ import unicode_literals

from django.db import migrations
def generate_center_link(apps, schema_editor):
    Acquisition = apps.get_model('annotations', 'Acquisition')
    CenterDictionary = apps.get_model('annotations', 'CenterDictionary')
    for acq in Acquisition.objects.all():
        center, created = CenterDictionary.objects.get_or_create(center_acronym=acq.center)
        acq.center_link = center
        acq.save()

class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0015_add_center_dictionary'),
    ]

    operations = [
        migrations.RunPython(generate_center_link),
    ]
