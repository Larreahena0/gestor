# Generated by Django 2.0.2 on 2020-07-09 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0018_auto_20200707_1630'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conv', '0006_documento_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento_Adjunto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('documento', models.FileField(null=True, upload_to='', verbose_name='Documento')),
                ('comentarios', models.TextField(max_length=400, null=True, verbose_name='Comentarios')),
                ('estado', models.CharField(max_length=100, null=True, verbose_name='Estado')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición')),
                ('id_documento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conv.Documento', verbose_name='Documento del semillero')),
            ],
            options={
                'verbose_name': 'Documento Adjunto',
                'verbose_name_plural': 'Documentos Adjuntos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición')),
                ('id_convocatoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conv.Convocatoria', verbose_name='Convocatoria')),
                ('id_semillero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='create.Semillero', verbose_name='Semillero Participante')),
            ],
            options={
                'verbose_name': 'Participante',
                'verbose_name_plural': 'Participantes',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='documento_adjunto',
            name='id_participante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conv.Participante', verbose_name='Semillero Participante'),
        ),
        migrations.AddField(
            model_name='documento_adjunto',
            name='id_usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
