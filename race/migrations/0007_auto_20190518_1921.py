# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-18 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0006_auto_20190518_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='race_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='race date'),
        ),
    ]