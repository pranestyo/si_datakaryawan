# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-04 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perusahaan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaftarPerusahaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diterima', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='karyawan',
            name='alamat',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='perusahaan',
            name='alamat',
            field=models.TextField(max_length=200),
        ),
        migrations.AddField(
            model_name='daftarperusahaan',
            name='nama_perusahaan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.Perusahaan'),
        ),
    ]
