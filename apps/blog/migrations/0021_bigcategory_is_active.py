# Generated by Django 2.2.5 on 2019-11-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20190912_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigcategory',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, verbose_name='是否在菜单栏显示'),
        ),
    ]
