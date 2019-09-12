# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-08-07 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190807_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecategory',
            name='description',
            field=models.TextField(default='KenZhang的个人博客，记录生活的瞬间，分享学习的心得，感悟生活，留住感动，静静寻觅生活的美好', help_text='用来作为SEO中description,长度参考SEO标准', max_length=240, verbose_name='描述'),
        ),
    ]
