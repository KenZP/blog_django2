# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-08-06 18:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_auto_20190806_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpro',
            old_name='nick_name',
            new_name='name',
        ),
    ]