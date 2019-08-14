from django.db import models
from core.models import Grupo
from workline.models import Linea

# Create your models here.
class Semillero(models.Model):
    grupos = Grupo.objects.all()
    lineas = Linea.objects.all()
    group_names = ((str(grupo.id), grupo.name) for grupo in grupos)
    line_names = ((str(linea.id), linea.name) for linea in lineas)
    id = models.AutoField(primary_key=True, verbose_name="Id")
    id_group = models.CharField(max_length=50, choices=group_names, verbose_name="Grupo", null=True)
    name = models.CharField(max_length=50, verbose_name="Nombre", null=True)
    lines = models.CharField(max_length=50, choices=line_names, verbose_name="Líneas de investigación", null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

    class Meta():
        verbose_name = "Semillero"
        verbose_name_plural = "Semilleros"
        ordering = ["id"]

    def __str__(self):
        return self.name