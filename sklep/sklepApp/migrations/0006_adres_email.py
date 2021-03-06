# Generated by Django 4.0.3 on 2022-03-06 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklepApp', '0005_alter_produkt_cena'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kraj', models.CharField(max_length=100)),
                ('miasto', models.CharField(max_length=100)),
                ('ulica', models.CharField(max_length=100)),
                ('nr_budynku', models.IntegerField()),
                ('nr_mieszkania', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
