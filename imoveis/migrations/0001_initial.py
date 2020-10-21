# Generated by Django 3.1 on 2020-08-25 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Alugado', 'Alugado'), ('Desocupado', 'Desocupado')], max_length=10)),
                ('fins', models.CharField(choices=[('Aluguel', 'Aluguel'), ('Venda', 'Venda')], max_length=10)),
                ('endereco', models.CharField(max_length=60)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=30)),
                ('garagem', models.IntegerField()),
                ('quartos', models.IntegerField()),
                ('banheiros', models.IntegerField()),
            ],
        ),
    ]