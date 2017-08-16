# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-04 02:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aktif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mulai_bekerja', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='AkunPerusahaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='KabupatenKota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kabupaten_kota', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Karyawan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_karyawan', models.CharField(max_length=50)),
                ('no_identitas', models.IntegerField()),
                ('pendidikan_terakhir', models.CharField(choices=[('sma_smk', 'SMA/SMK'), ('d1', 'D1'), ('d2', 'D2'), ('d3', 'D3'), ('s1', 'S1'), ('s2', 'S2'), ('s3', 'S3')], max_length=50)),
                ('jurusan', models.CharField(max_length=50)),
                ('alamat', models.TextField(max_length=50)),
                ('jenis_kelamin', models.CharField(choices=[('pria', 'Pria'), ('wanita', 'Wanita')], max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('telepon', models.CharField(max_length=15)),
                ('gaji', models.IntegerField()),
                ('jabatan', models.CharField(max_length=50)),
                ('divisi', models.CharField(max_length=50)),
                ('status_karyawan', models.CharField(max_length=20)),
                ('nama_kabupaten_kota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.KabupatenKota')),
            ],
        ),
        migrations.CreateModel(
            name='Kecamatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kecamatan', models.CharField(max_length=50)),
                ('nama_kabupaten_kota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.KabupatenKota')),
            ],
        ),
        migrations.CreateModel(
            name='Perusahaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_perusahaan', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=40)),
                ('alamat', models.TextField(max_length=50)),
                ('telepon', models.CharField(max_length=15)),
                ('produk_utama', models.CharField(max_length=50)),
                ('tenaga_kerja', models.IntegerField()),
                ('nama_kabupaten_kota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.KabupatenKota')),
                ('nama_kecamatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.Kecamatan')),
            ],
        ),
        migrations.CreateModel(
            name='Provinsi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_provinsi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Resign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('akhir_bekerja', models.DateField()),
                ('mulai_bekerja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.Aktif')),
                ('nama_karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.Karyawan')),
            ],
        ),
        migrations.AddField(
            model_name='perusahaan',
            name='nama_provinsi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.Provinsi'),
        ),
        migrations.AddField(
            model_name='karyawan',
            name='nama_kecamatan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.Kecamatan'),
        ),
        migrations.AddField(
            model_name='karyawan',
            name='nama_perusahaan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.Perusahaan'),
        ),
        migrations.AddField(
            model_name='karyawan',
            name='nama_provinsi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.Provinsi'),
        ),
        migrations.AddField(
            model_name='kabupatenkota',
            name='nama_provinsi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.Provinsi'),
        ),
        migrations.AddField(
            model_name='aktif',
            name='nama_karyawan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.Karyawan'),
        ),
    ]
