# Generated by Django 2.2.4 on 2020-03-13 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0008_auto_20200313_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrante',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
