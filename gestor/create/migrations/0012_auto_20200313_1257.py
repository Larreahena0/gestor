# Generated by Django 2.2.4 on 2020-03-13 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0011_lineasemillero_id_coo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lineasemillero',
            old_name='id_coo',
            new_name='id_sem',
        ),
    ]