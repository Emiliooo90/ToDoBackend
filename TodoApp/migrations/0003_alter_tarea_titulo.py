# Generated by Django 4.2.2 on 2024-01-23 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0002_alter_tarea_descripcion_alter_tarea_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='titulo',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]