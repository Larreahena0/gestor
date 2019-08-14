from django.db import models

# Create your models here.
class Grupo(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True, verbose_name="Id")
    name = models.CharField(max_length=50, verbose_name="Nombre del grupo:", null=True)
    coordinator = models.CharField(max_length=50, verbose_name="Coordinador(a) del grupo", null=True)

    class Meta():
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
        ordering = ["name"]

    def __str__(self):
        return self.name