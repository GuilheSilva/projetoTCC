# Generated by Django 3.1 on 2020-10-18 02:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0047_auto_20201017_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='data',
            field=models.DateField(default=datetime.datetime(2020, 10, 17, 23, 13, 23, 174419)),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2020, 10, 17, 23, 13, 23, 175419)),
        ),
    ]