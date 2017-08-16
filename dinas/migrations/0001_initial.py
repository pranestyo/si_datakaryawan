# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-05 13:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perusahaan', '0002_auto_20170604_1033'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AkunDinas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('akun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('kabupatenkota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.KabupatenKota')),
            ],
        ),
        migrations.CreateModel(
            name='TampilDinas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah_karyawan_aktif', models.IntegerField()),
                ('jumlah_karyawan_resign', models.IntegerField()),
                ('tingkat_pendidikan', models.CharField(max_length=20)),
                ('rentang_gaji', models.IntegerField()),
                ('nama_kabupaten_kota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.KabupatenKota')),
            ],
        ),
    ]
