# Generated by Django 4.1.2 on 2022-11-15 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_alter_paciente_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='consulta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('telefono', models.CharField(max_length=9, verbose_name='Telefono')),
                ('medico', models.CharField(max_length=30, verbose_name='Medico')),
                ('razon', models.CharField(max_length=300, verbose_name='Motivo')),
                ('valor', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
    ]