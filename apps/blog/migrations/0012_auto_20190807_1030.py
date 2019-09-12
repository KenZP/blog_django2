# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-08-07 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190807_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, default='', null=True, verbose_name='公告')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否开启')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='提交日期')),
            ],
            options={
                'verbose_name': '公告',
                'verbose_name_plural': '公告',
                'ordering': ['add_date'],
            },
        ),
        migrations.DeleteModel(
            name='Notice',
        ),
    ]