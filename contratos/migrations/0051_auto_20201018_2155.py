# Generated by Django 3.1 on 2020-10-19 00:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0050_auto_20201018_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Em aberto')], default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='data',
            field=models.DateField(default=datetime.datetime(2020, 10, 18, 21, 55, 24, 45453)),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2020, 10, 18, 21, 55, 24, 50448)),
        ),
    ]
