# Generated by Django 3.1 on 2020-10-09 23:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0030_auto_20201009_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='data',
            field=models.DateField(default=datetime.datetime(2020, 10, 9, 20, 58, 59, 715376)),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2020, 10, 9, 20, 58, 59, 716376)),
        ),
    ]
