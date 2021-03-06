# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-17 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acquisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_scan', models.DateField(blank=True, null=True)),
                ('center', models.CharField(blank=True, max_length=32, null=True)),
                ('scanner', models.CharField(blank=True, max_length=32, null=True)),
                ('study', models.CharField(blank=True, max_length=64, null=True)),
                ('subject', models.CharField(blank=True, max_length=64, null=True)),
                ('dataset_file', models.BooleanField(default=False, verbose_name='Dataset description exists')),
            ],
        ),
        migrations.CreateModel(
            name='Demographic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(default='unknown', max_length=64)),
                ('family_name', models.CharField(default='unknown', max_length=64)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('pathology', models.CharField(blank=True, max_length=128, null=True)),
                ('researcher', models.CharField(blank=True, max_length=128, null=True)),
                ('acquisition', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='demographic', to='annotations.Acquisition')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contrast', models.CharField(max_length=16)),
                ('filename', models.FilePathField(match='*.nii.gz', verbose_name='/')),
                ('start_coverage', models.CharField(blank=True, max_length=16, null=True)),
                ('end_coverage', models.CharField(blank=True, max_length=16, null=True)),
                ('orientation', models.CharField(blank=True, max_length=16, null=True)),
                ('resolution', models.CharField(blank=True, max_length=16, null=True)),
                ('pam50', models.BooleanField(default=False)),
                ('ms_mapping', models.BooleanField(default=False)),
                ('gm_model', models.BooleanField(default=False)),
                ('acquisition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='annotations.Acquisition')),
            ],
        ),
        migrations.CreateModel(
            name='LabeledImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(choices=[('seg_manual', 'Binary mask of spinal cord'), ('gmseg_manual', 'Binary mask of gray matter'), ('lesion_manual', 'Binary mask of lesions'), ('labels_disc', 'Single voxel at the posterior tip of each inter-vertebral disc')], max_length=16)),
                ('filename', models.FilePathField(match='*.nii.gz', verbose_name='/')),
                ('author', models.CharField(blank=True, max_length=64, null=True)),
                ('contrast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labeled_images', to='annotations.Image')),
            ],
        ),
    ]
