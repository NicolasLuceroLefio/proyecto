# Generated by Django 5.0.6 on 2024-10-20 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='fecha_final',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_inicio',
            field=models.DateField(null=True),
        ),
    ]
