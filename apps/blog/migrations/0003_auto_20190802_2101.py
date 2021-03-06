# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-08-02 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190728_2013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-add_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(default='', max_length=300, upload_to='banner/%Y/%m', verbose_name='图片'),
        ),
    ]
