# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-08-07 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190807_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigcategory',
            name='description',
            field=models.TextField(default='', max_length=50, verbose_name='大分类描述'),
        ),
    ]
