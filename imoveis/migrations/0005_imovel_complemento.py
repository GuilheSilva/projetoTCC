# Generated by Django 3.1 on 2020-09-30 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0004_delete_importimoveis'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='complemento',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
