# Generated by Django 4.1.2 on 2022-11-16 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0004_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='fecha',
            field=models.DateField(verbose_name='fecha consulta'),
        ),
    ]
