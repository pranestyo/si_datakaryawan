# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-10 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perusahaan', '0002_auto_20170604_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daftarperusahaan',
            name='nama_perusahaan',
        ),
        migrations.AddField(
            model_name='perusahaan',
            name='diterima',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='DaftarPerusahaan',
        ),
    ]
