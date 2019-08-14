from django.db import models
from create.models import Semillero

# Create your models here.


class Integrante(models.Model):
    semilleros = Semillero.objects.all()
    semillero_names = ((str(semillero.id), semillero.name) for semillero in semilleros)
    rols = (
        ('1', 'Estudiante'),
        ('2', 'Coordinador'),
    )
    career_names = (
        ('1', 'Ay, el DHL'),
        ('2', '¿Dónde está mi puto DHL?'),
    )
    name = models.CharField(max_length=100, verbose_name="Nombre del integrante", null=True)
    document = models.CharField(max_length=12, primary_key=True, verbose_name="Documento de identidad")
    semillero = models.CharField(max_length=100, choices=semillero_names, verbose_name="Semillero", null=True)
    rol = models.PositiveSmallIntegerField(verbose_name="Rol", choices=rols, null=True)
    joined = models.DateField(verbose_name="Fecha de ingreso", null=True)
    email = models.EmailField(verbose_name="Correo electrónico", null=True)
    career = models.CharField(max_length=50, choices=career_names, verbose_name="Programa de pregrado", null=True)
    level = models.PositiveSmallIntegerField(verbose_name="Nivel en el programa", null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

    class Meta():
        verbose_name = "Integrante"
        verbose_name_plural = "Integrantes"
        ordering = ["-joined"]

    def __str__(self):
        return self.name