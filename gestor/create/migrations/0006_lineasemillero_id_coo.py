# Generated by Django 2.2.4 on 2020-03-13 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0005_auto_20190902_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineasemillero',
            name='id_coo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='create.Integrante', verbose_name='Id del coordinador'),
        ),
    ]
