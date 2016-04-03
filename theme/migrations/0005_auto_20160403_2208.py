# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 19:08
from __future__ import unicode_literals

import datetime
from django.db import migrations
from django.utils.timezone import utc
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0004_auto_20160403_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='team_image',
            field=mezzanine.core.fields.FileField(default=datetime.datetime(2016, 4, 3, 19, 8, 30, 91044, tzinfo=utc), max_length=200, verbose_name='File'),
            preserve_default=False,
        ),
    ]