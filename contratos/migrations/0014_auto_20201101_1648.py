# Generated by Django 3.1 on 2020-11-01 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0013_auto_20201101_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='data',
            field=models.DateField(default=datetime.datetime(2020, 11, 1, 16, 48, 13, 744938)),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2020, 11, 1, 16, 48, 13, 746938)),
        ),
    ]