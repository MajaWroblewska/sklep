# Generated by Django 4.0.3 on 2022-03-06 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sklepApp', '0009_rename_kategoria_id_produkt_kategoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produkt',
            old_name='kategoria',
            new_name='kategoria_id',
        ),
    ]
