# Generated by Django 2.2.4 on 2020-01-27 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20200127_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Imagen'),
        ),
    ]
