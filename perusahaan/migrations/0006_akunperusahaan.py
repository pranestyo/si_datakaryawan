# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-13 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perusahaan', '0005_auto_20170613_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='AkunPerusahaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=50)),
                ('perusahaan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.Perusahaan')),
            ],
        ),
    ]