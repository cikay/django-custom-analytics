# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2021-05-23 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_auto_20210523_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='nick_name',
            field=models.CharField(default='no nick name', max_length=50),
            preserve_default=False,
        ),
    ]
