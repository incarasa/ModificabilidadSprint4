# Generated by Django 4.2.17 on 2024-12-04 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manejador_cronogramas', '0004_remove_estudiante_cronograma_estudiante_cronogramas_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pago',
            name='nombre',
        ),
    ]
