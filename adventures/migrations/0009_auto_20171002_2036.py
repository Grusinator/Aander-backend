# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventures', '0008_auto_20171001_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='title',
            field=models.CharField(default='test_location', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clue',
            name='clue_image',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
