# Generated by Django 3.1 on 2020-10-18 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0005_imovel_complemento'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='cep',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]