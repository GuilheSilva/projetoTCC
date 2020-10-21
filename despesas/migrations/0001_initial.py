# Generated by Django 3.1 on 2020-09-27 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('imoveis', '0003_importimoveis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Manutenção', 'Manutenção')], max_length=10)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateField()),
                ('observacao', models.TextField()),
                ('id_user', models.IntegerField()),
                ('imoveis', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='imoveis.imovel')),
            ],
        ),
    ]