# Generated by Django 4.2.16 on 2024-11-12 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Medicos', '0002_alter_medicos_apellidos_alter_medicos_direccion_and_more'),
        ('Examen', '0002_examen_medicos_examen_paciente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='examen',
            options={'verbose_name_plural': 'Exámenes'},
        ),
        migrations.RemoveField(
            model_name='examen',
            name='Nombres',
        ),
        migrations.RemoveField(
            model_name='examen',
            name='medicos',
        ),
        migrations.AddField(
            model_name='examen',
            name='medico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Medicos.medicos', verbose_name='Medico'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detalleexamen',
            name='examen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Examen.examen', verbose_name='Examen'),
        ),
    ]
