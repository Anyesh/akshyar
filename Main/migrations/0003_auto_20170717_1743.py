# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_delete_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='aakshyarurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='aakshyarurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=25, unique=True),
        ),
    ]
