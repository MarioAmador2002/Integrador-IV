# Generated by Django 4.2.16 on 2024-11-09 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Citas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoCitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=50)),
                ('Fecha_Registro', models.DateField()),
                ('citas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Citas.citas', verbose_name='Citas')),
            ],
            options={
                'verbose_name_plural': 'EstadosCitas',
            },
        ),
    ]
