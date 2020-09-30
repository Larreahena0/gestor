# Generated by Django 2.0.2 on 2020-09-29 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0028_auto_20200917_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atributos_otra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('tipo', models.CharField(max_length=100, null=True, verbose_name='Tipo')),
                ('id_estudiante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='create.Integrante', verbose_name='Estudiante')),
            ],
            options={
                'verbose_name': 'Atributo',
                'verbose_name_plural': 'Atributos otra universidad',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='semillero',
            name='image',
            field=models.FileField(default='/logo_udea.png', null=True, upload_to='', verbose_name='Imagen del semillero'),
        ),
    ]
