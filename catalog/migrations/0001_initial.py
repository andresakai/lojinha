# Generated by Django 3.1.3 on 2020-11-23 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['name'],
            },
        ),
    ]