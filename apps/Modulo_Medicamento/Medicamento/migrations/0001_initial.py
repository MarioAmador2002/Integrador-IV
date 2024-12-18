# Generated by Django 4.2.16 on 2024-11-09 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pacientes', '0001_initial'),
        ('Enfermedad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('Descripcion', models.CharField(max_length=50, verbose_name='Descripcion')),
                ('NombreGenerico', models.CharField(max_length=50, verbose_name='NombreGenerico')),
                ('Presentacion', models.CharField(max_length=50, verbose_name='Presentacion')),
                ('Contradicciones', models.CharField(max_length=50, verbose_name='Contradicciones')),
                ('EfectosSecundarios', models.CharField(max_length=50, verbose_name='EfectosSecundarios')),
            ],
            options={
                'verbose_name_plural': 'Medicamentos',
            },
        ),
        migrations.CreateModel(
            name='DetalleMedicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Receta', models.CharField(max_length=100)),
                ('Dosis', models.CharField(max_length=100)),
                ('Frecuencia', models.CharField(max_length=100)),
                ('Duracion', models.CharField(max_length=100)),
                ('Indicacion', models.CharField(max_length=100)),
                ('enfermedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enfermedad.enfermedad', verbose_name='Enfermedad')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medicamento.medicamento', verbose_name='Medicamento')),
                ('pacientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pacientes.pacientes', verbose_name='Pacientes')),
            ],
            options={
                'verbose_name_plural': 'DetalleMedicamentos',
            },
        ),
    ]
