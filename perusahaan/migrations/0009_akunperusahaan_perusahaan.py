# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-28 05:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perusahaan', '0008_remove_akunperusahaan_perusahaan'),
    ]

    operations = [
        migrations.AddField(
            model_name='akunperusahaan',
            name='perusahaan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='perusahaan.Perusahaan'),
            preserve_default=False,
        ),
    ]
