# Generated by Django 2.2.4 on 2020-03-13 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0010_remove_lineasemillero_id_coo'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineasemillero',
            name='id_coo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='create.Semillero', verbose_name='Id del coordinador'),
        ),
    ]