# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-01-15 10:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20200115_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='descript',
        ),
    ]