# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2021-05-23 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0011_auto_20210523_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translator',
            name='added_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
