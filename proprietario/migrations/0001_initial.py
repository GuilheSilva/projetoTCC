# Generated by Django 3.1 on 2020-10-24 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proprietarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('identidade', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('password2', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.CharField(max_length=30)),
                ('numero', models.CharField(max_length=30)),
                ('bairro', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=30)),
                ('userid', models.IntegerField()),
            ],
        ),
    ]
