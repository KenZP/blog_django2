# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-07-26 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20190726_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpro',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=5),
        ),
        migrations.AlterField(
            model_name='userpro',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='users/%Y/%m', verbose_name='用户图像'),
        ),
    ]