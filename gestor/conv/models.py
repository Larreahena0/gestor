from django.db import models

# Creamos el modelo convocatoria
class Convocatoria(models.Model):
    # Definimos siete campos con sus respectivos parametros
    id = models.AutoField(primary_key=True, verbose_name="Id")
    name = models.CharField(max_length=100, verbose_name="Nombre de la convocatoria", null=True)
    description = models.TextField(max_length=400, verbose_name="Descripción", null=True)
    opened = models.DateField(verbose_name="Fecha de apertura", null=True)
    closed = models.DateField(verbose_name="Fecha de cierre", null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

    # Asignamos un nombre a la tabla y ordenamos por fecha de cierre
    class Meta():
        verbose_name = "Convocatoria"
        verbose_name_plural = "Convocatorias"
        ordering = ["closed"]

    # Definimos el parametro principal del modelo, por el cual lo identificaremos
    # en este caso es el nombre
    def __str__(self):
        return self.name

# Creamos el modelo documento
class Documento(models.Model):
    # Definimos siete campos con sus respectivos parametros
    id = models.AutoField(primary_key=True, verbose_name="Id")
    id_conv = models.ForeignKey(Convocatoria, null=True, blank=True, on_delete=models.CASCADE)
    documento = models.FileField(verbose_name="Documento", null=True)
    description = models.TextField(max_length=400, verbose_name="Descripción", null=True)
    tipo = models.PositiveSmallIntegerField(verbose_name="Tipo", null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

    # Asignamos un nombre a la tabla y agrupamos por convocatorias a las que pertenecen
    class Meta():
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        ordering = ["id_conv"]

    # Definimos el parametro principal del modelo, por el cual lo identificaremos
    # en este caso es la descripción
    def __str__(self):
        return self.description
