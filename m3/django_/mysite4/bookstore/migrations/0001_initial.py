# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-01-16 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=11, unique=True, verbose_name='书名')),
                ('pub', models.CharField(max_length=50, verbose_name='出版社')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='定价')),
                ('market_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='零售价')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
    ]
