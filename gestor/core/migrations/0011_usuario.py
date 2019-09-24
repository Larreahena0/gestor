# Generated by Django 2.2.4 on 2019-09-07 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('username', models.CharField(max_length=50, null=True, verbose_name='Nombre de usuario:')),
                ('password', models.CharField(max_length=50, null=True, verbose_name='Contraseña:')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Nombre::')),
                ('lastname', models.CharField(max_length=50, null=True, verbose_name='Apellidos::')),
                ('email', models.EmailField(max_length=50, null=True, verbose_name='Correo electrónico:')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['lastname'],
            },
        ),
    ]