from django.db import models

# Create your models here.
class Semillero(models.Model):

	id = models.AutoField(primary_key=True, verbose_name="Id")
	id_group = models.CharField(max_length=50, verbose_name="Grupo", null=True)
	name = models.CharField(max_length=50, verbose_name="Nombre", null=True)
	history = models.TextField(verbose_name="Antesedentes", null=True)
	mision = models.TextField(verbose_name="Misión", null=True)
	vision = models.TextField(verbose_name="Visión", null=True)
	goals = models.TextField(verbose_name="Objetivos", null=True)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

	class Meta():
		verbose_name = "Semillero"
		verbose_name_plural = "Semilleros"
		ordering = ["id"]

	def __str__(self):
		return self.name

class Integrante(models.Model):

	id = models.AutoField(primary_key=True, verbose_name="Id del integrante")
	name = models.CharField(max_length=100, verbose_name="Nombre del integrante", null=True)
	document = models.CharField(max_length=12, verbose_name="Documento de identidad", null=True)
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

class LineaSemillero(models.Model):

	id = models.AutoField(primary_key=True, verbose_name="Id")
	id_coo = models.ForeignKey(Integrante, verbose_name="Coordinador", null=True, blank=True, on_delete=models.CASCADE)
	id_linea = models.PositiveSmallIntegerField(verbose_name="Id de la línea", null=True)
	name = models.CharField(max_length=100, verbose_name="Linea de investigación", null=True)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

	class Meta():
		verbose_name = "Línea por coordinador"
		verbose_name_plural = "Líneas por coordinador"
		ordering = ["-created"]

	def __str__(self):
		return self.name

class Career(models.Model):
	id = models.PositiveIntegerField(primary_key=True, verbose_name="Id")
	name = models.CharField(max_length=100, null=True)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

	class Meta():
		verbose_name = "Pregrado"
		verbose_name_plural = "Pregrados"
		ordering = ["id"]

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
