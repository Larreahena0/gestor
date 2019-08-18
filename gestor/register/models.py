from django.db import models

# Create your models here.


class Integrante(models.Model):
    
    name = models.CharField(max_length=100, verbose_name="Nombre del integrante", null=True)
    document = models.CharField(max_length=12, primary_key=True, verbose_name="Documento de identidad")
    semillero = models.CharField(max_length=100, verbose_name="Semillero", null=True)
    rol = models.PositiveSmallIntegerField(verbose_name="Rol", null=True)
    joined = models.DateField(verbose_name="Fecha de ingreso", null=True)
    email = models.EmailField(verbose_name="Correo electrónico", null=True)
    career = models.CharField(max_length=50, verbose_name="Programa de pregrado", null=True)
    level = models.PositiveSmallIntegerField(verbose_name="Nivel en el programa", null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

    class Meta():
        verbose_name = "Integrante"
        verbose_name_plural = "Integrantes"
        ordering = ["-joined"]

    def __str__(self):
        return self.name