# Generated by Django 2.2.4 on 2019-10-30 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conv', '0005_documento'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='tipo',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Tipo'),
        ),
    ]
