# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-23 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perusahaan', '0013_auto_20170716_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MonthlyRevenue', models.CharField(max_length=50)),
                ('Month', models.CharField(max_length=50)),
            ],
        ),
    ]