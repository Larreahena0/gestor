from django.db import models

# Create your models here.
class Linea(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    name = models.CharField(max_length=100, verbose_name="Linea de investigación", null=True)
    description = models.TextField(max_length=400, verbose_name="Descripción", null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

    class Meta():
        verbose_name = "Línea"
        verbose_name_plural = "Líneas"
        ordering = ["-created"]

    def __str__(self):
        return self.name