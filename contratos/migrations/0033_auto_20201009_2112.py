# Generated by Django 3.1 on 2020-10-10 00:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0032_auto_20201009_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='data',
            field=models.DateField(default=datetime.datetime(2020, 10, 9, 21, 11, 57, 584344)),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2020, 10, 9, 21, 11, 57, 584344)),
        ),
    ]
