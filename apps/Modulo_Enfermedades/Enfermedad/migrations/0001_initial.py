# Generated by Django 4.2.16 on 2024-11-09 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('Descripcion', models.CharField(max_length=80, verbose_name='Descripcion')),
                ('Sintomas', models.CharField(max_length=80, verbose_name='Sintoma')),
                ('Tratamiento', models.CharField(max_length=80, verbose_name='Tratamientos')),
                ('pacientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pacientes.pacientes', verbose_name='pacientes')),
            ],
            options={
                'verbose_name_plural': 'Enfermedad',
            },
        ),
        migrations.CreateModel(
            name='DetalleEnfermedades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tratamiento', models.CharField(max_length=50, verbose_name='tratamiento')),
                ('Fecha_registro', models.CharField(max_length=50, verbose_name='fecha de registro')),
                ('enfermedades', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enfermedad.enfermedad', verbose_name='Enfermedad')),
                ('pacientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pacientes.pacientes', verbose_name='Pacientes')),
            ],
            options={
                'verbose_name_plural': 'DetalleEnfermedades',
            },
        ),
    ]
