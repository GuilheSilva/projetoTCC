# Generated by Django 3.1 on 2020-10-17 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0040_merge_20201013_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='data',
            field=models.DateField(default=datetime.datetime(2020, 10, 17, 18, 27, 46, 645347)),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2020, 10, 17, 18, 27, 46, 646347)),
        ),
    ]