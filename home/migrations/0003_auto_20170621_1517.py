# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 15:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170620_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='calculationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
