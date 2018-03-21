# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-22 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0008_auto_20180316_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='filestate',
            field=models.CharField(choices=[('OK', 'File is available'), ('NA', 'File not available'), ('ERR', 'File error')], default='OK', max_length=3, verbose_name='The state of the file'),
        ),
        migrations.AddField(
            model_name='labeledimage',
            name='filestate',
            field=models.CharField(choices=[('OK', 'File is available'), ('NA', 'File not available'), ('ERR', 'File error')], default='OK', max_length=3, verbose_name='The state of the file'),
        ),
        migrations.AlterField(
            model_name='image',
            name='filename',
            field=models.CharField(max_length=512, verbose_name='File path: (/Volumes/sct_testing/large/)'),
        ),
        migrations.AlterField(
            model_name='image',
            name='gm_model',
            field=models.BooleanField(default=False, help_text='Is image used to model gray matter'),
        ),
        migrations.AlterField(
            model_name='image',
            name='ms_mapping',
            field=models.BooleanField(default=False, help_text='Is image used in mapping MS'),
        ),
        migrations.AlterField(
            model_name='image',
            name='pam50',
            field=models.BooleanField(default=False, help_text='Is image used in the generation of PAM50'),
        ),
        migrations.AlterField(
            model_name='labeledimage',
            name='filename',
            field=models.CharField(max_length=512, verbose_name='File path: (/Volumes/sct_testing/large/)'),
        ),
        migrations.AlterField(
            model_name='labeledimage',
            name='label',
            field=models.CharField(choices=[('seg_manual', 'Binary mask of spinal cord'), ('gmseg_manual', 'Binary mask of gray matter'), ('lesion_manual', 'Binary mask of lesions'), ('labels_disc', 'Single voxel at the posterior tip of each inter-vertebral disc')], help_text='What type of labeled image', max_length=16),
        ),
    ]
