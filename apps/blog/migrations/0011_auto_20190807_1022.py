# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-08-07 10:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190807_0954'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Activate',
            new_name='Notice',
        ),
    ]
