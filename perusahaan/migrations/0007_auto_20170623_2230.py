# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-23 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perusahaan', '0006_akunperusahaan'),
    ]

    operations = [
        migrations.AddField(
            model_name='resign',
            name='surat_keterangan',
            field=models.FileField(blank=True, upload_to='C:\\Users\\DESI\\si_dk\\assets/file_upload'),
        ),
        migrations.AlterField(
            model_name='aktif',
            name='foto',
            field=models.ImageField(blank=True, upload_to='C:\\Users\\DESI\\si_dk\\assets/image_upload'),
        ),
    ]