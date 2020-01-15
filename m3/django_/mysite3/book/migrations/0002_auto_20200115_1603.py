# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-01-15 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='descript',
            field=models.CharField(default='', max_length=50, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='定价'),
        ),
    ]