# Generated by Django 2.2.5 on 2020-06-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200630_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpro',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=5),
        ),
    ]