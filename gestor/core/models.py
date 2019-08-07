from django.db import models

# Create your models here.
class GrupoInvestigacion(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.TextField()
    coordinador = models.TextField()