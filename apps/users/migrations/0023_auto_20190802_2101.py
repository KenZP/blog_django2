# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-08-02 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20190727_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpro',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=5),
        ),
    ]
