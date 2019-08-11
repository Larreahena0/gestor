from django.db import models

# Create your models here.
class Semillero(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    id_group = models.PositiveSmallIntegerField(verbose_name="Grupo", null=True)
    name = models.CharField(max_length=50, verbose_name="Nombre", null=True)
    lines = models.CharField(max_length=50, verbose_name="Líneas de investigación", null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

    class Meta():
        verbose_name = "Semillero"
        verbose_name_plural = "Semilleros"
        ordering = ["id"]

    def __str__(self):
        return self.name

class Integrante(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del integrante", null=True)
    document = models.PositiveIntegerField(primary_key=True, verbose_name="Documento de identidad")
    rol = models.PositiveSmallIntegerField(verbose_name="Rol", null=True)
    joined = models.DateTimeField(verbose_name="Fecha de ingreso", null=True)
    email = models.EmailField(verbose_name="Correo electrónico", null=True)
    career = models.TextField(verbose_name="Programa de pregrado", null=True)
    level = models.PositiveSmallIntegerField(verbose_name="Nivel en el programa", null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

    class Meta():
        verbose_name = "Integrante"
        verbose_name_plural = "Integrantes"
        ordering = ["-joined"]

    def __str__(self):
        return self.name

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

class Convocatoria(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    name = models.CharField(max_length=100, verbose_name="Nombre de la convocatoria", null=True)
    description = models.TextField(max_length=400, verbose_name="Descripción", null=True)
    opened = models.DateField(verbose_name="Fecha de apertura", null=True)
    closed = models.DateField(verbose_name="Fecha de cierre", null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

    class Meta():
        verbose_name = "Convocatoria"
        verbose_name_plural = "Convocatorias"
        ordering = ["-opened"]

    def __str__(self):
        return self.name

