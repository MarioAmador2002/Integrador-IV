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
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=60, verbose_name='Descripcion')),
                ('pacientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pacientes.pacientes', verbose_name='Pacientes')),
            ],
            options={
                'verbose_name_plural': 'Genero',
            },
        ),
    ]
