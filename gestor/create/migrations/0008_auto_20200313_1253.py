# Generated by Django 2.2.4 on 2020-03-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0007_remove_lineasemillero_id_sem'),
    ]

    operations = [
        migrations.AddField(
            model_name='integrante',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False, verbose_name='Id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='integrante',
            name='document',
            field=models.CharField(max_length=12, null=True, verbose_name='Documento de identidad'),
        ),
    ]
