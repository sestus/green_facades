# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 18:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0002_auto_20160403_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='team_image',
            field=models.ImageField(blank=True, default=datetime.datetime(2016, 4, 3, 18, 55, 6, 730303, tzinfo=utc), upload_to=''),
            preserve_default=False,
        ),
    ]
