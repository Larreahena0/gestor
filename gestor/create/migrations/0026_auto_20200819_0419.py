# Generated by Django 2.0.2 on 2020-08-19 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0025_lineasemillero_id_participante'),
    ]

    operations = [
        migrations.AddField(
            model_name='semillero',
            name='image',
            field=models.FileField(null=True, upload_to='', verbose_name='Imagen del semillero'),
        ),
        migrations.AddField(
            model_name='semillero',
            name='mail',
            field=models.TextField(null=True, verbose_name='Correo de contacto'),
        ),
    ]
