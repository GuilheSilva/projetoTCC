# Generated by Django 3.1 on 2020-10-18 23:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0049_auto_20201017_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='data',
            field=models.DateField(default=datetime.datetime(2020, 10, 18, 20, 2, 1, 263121)),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2020, 10, 18, 20, 2, 1, 265121)),
        ),
    ]