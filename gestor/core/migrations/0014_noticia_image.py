# Generated by Django 2.2.4 on 2020-01-27 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200126_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Imagen'),
        ),
    ]
