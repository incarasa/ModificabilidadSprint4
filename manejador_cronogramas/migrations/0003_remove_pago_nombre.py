# Generated by Django 4.2.17 on 2024-12-04 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manejador_cronogramas', '0002_remove_cronograma_estudiante_estudiante_cronograma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pago',
            name='nombre',
        ),
    ]
