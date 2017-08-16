# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-13 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('perusahaan', '0003_auto_20170610_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aktif',
            old_name='nama_karyawan',
            new_name='karyawan',
        ),
        migrations.RenameField(
            model_name='kabupatenkota',
            old_name='nama_provinsi',
            new_name='provinsi',
        ),
        migrations.RenameField(
            model_name='karyawan',
            old_name='nama_kabupaten_kota',
            new_name='kabupatenkota',
        ),
        migrations.RenameField(
            model_name='karyawan',
            old_name='nama_kecamatan',
            new_name='kecamatan',
        ),
        migrations.RenameField(
            model_name='karyawan',
            old_name='nama_perusahaan',
            new_name='perusahaan',
        ),
        migrations.RenameField(
            model_name='karyawan',
            old_name='nama_provinsi',
            new_name='provinsi',
        ),
        migrations.RenameField(
            model_name='kecamatan',
            old_name='nama_kabupaten_kota',
            new_name='kabupatenkota',
        ),
        migrations.RenameField(
            model_name='perusahaan',
            old_name='nama_kabupaten_kota',
            new_name='kabupatenkota',
        ),
        migrations.RenameField(
            model_name='perusahaan',
            old_name='nama_kecamatan',
            new_name='kecamatan',
        ),
        migrations.RenameField(
            model_name='perusahaan',
            old_name='nama_provinsi',
            new_name='provinsi',
        ),
        migrations.RenameField(
            model_name='resign',
            old_name='mulai_bekerja',
            new_name='aktif',
        ),
        migrations.RenameField(
            model_name='resign',
            old_name='nama_karyawan',
            new_name='karyawan',
        ),
        migrations.AddField(
            model_name='aktif',
            name='foto',
            field=models.ImageField(blank=True, upload_to='C:\\Users\\DESI\\si_dk\\assets/upload'),
        ),
        migrations.AddField(
            model_name='akunperusahaan',
            name='perusahaan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='perusahaan.Perusahaan'),
            preserve_default=False,
        ),
    ]
