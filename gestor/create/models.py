from django.db import models
from django.contrib.auth.models import User
from core.models import Grupo

# Create your models here.
class Integrante(models.Model):

	id = models.AutoField(primary_key=True, verbose_name="Id del integrante")
	name = models.CharField(max_length=100, verbose_name="Nombre del integrante", null=True)
	lastname = models.CharField(max_length=100, verbose_name="Apellidos del integrante", null=True)
	document = models.CharField(max_length=12, verbose_name="Documento de identidad", null=True)
	email = models.EmailField(verbose_name="Correo electrónico", null=True)
	phone = models.CharField(max_length=50, verbose_name="Telefono", null=True)
	aditional = models.CharField(max_length=100, verbose_name="Informacion Adicional", null=True)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

	class Meta():
		verbose_name = "Integrante"
		verbose_name_plural = "Integrantes"
		ordering = ["-id"]

	def __str__(self):
		return self.name

class Semillero(models.Model):

	id = models.AutoField(primary_key=True, verbose_name="Id")
	id_group = models.ForeignKey(Grupo, verbose_name="Grupo de investigacion", null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, verbose_name="Nombre", null=True)
	history = models.TextField(verbose_name="Antesedentes", null=True)
	mision = models.TextField(verbose_name="Misión", null=True)
	vision = models.TextField(verbose_name="Visión", null=True)
	goals = models.TextField(verbose_name="Objetivos", null=True)
	coordinador = models.ForeignKey(Integrante, verbose_name="coordinador", null=True, blank=True, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

	class Meta():
		verbose_name = "Semillero"
		verbose_name_plural = "Semilleros"
		ordering = ["id"]

	def __str__(self):
		return self.name

class Rol(models.Model):
	id = models.AutoField(primary_key=True, verbose_name="Id")
	name = models.CharField(max_length=100, verbose_name="Nombre del rol", null=True)
	description = models.TextField(verbose_name="Descripcion", null=True)
	
	class Meta():
		verbose_name = "Rol"
		verbose_name_plural = "Roles"
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

class Career(models.Model):
	id = models.AutoField(primary_key=True, verbose_name="Id")
	name = models.CharField(max_length=100, null=True,verbose_name="Nombre")
	tipo = models.CharField(max_length=100, null=True,verbose_name="Tipo")
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

	class Meta():
		verbose_name = "Programa"
		verbose_name_plural = "Programas"
		ordering = ["id"]

	def __str__(self):
		return self.name

class Participante2(models.Model):
	id = models.AutoField(primary_key=True, verbose_name="Id")
	id_integrante = models.ForeignKey(Integrante, verbose_name="Integrante", null=True, blank=True, on_delete=models.CASCADE)
	id_semillero = models.ForeignKey(Semillero, verbose_name="Semillero", null=True, blank=True, on_delete=models.CASCADE)
	rol = models.ForeignKey(Rol,verbose_name="Rol", null=True,on_delete=models.CASCADE)
	joined = models.DateField(verbose_name="Fecha de ingreso", null=True)

	class Meta():
		verbose_name = "Participante"
		verbose_name_plural = "Participantes"
		ordering = ["id"]

	def __str__(self):
		return self.id_integrante.name

class Atributos(models.Model):
	id = models.AutoField(primary_key=True, verbose_name="Id")
	id_estudiante = models.ForeignKey(Integrante, verbose_name="Estudiante", null=True, blank=True, on_delete=models.CASCADE)
	id_programa = models.ForeignKey(Career, verbose_name="Programa", null=True, blank=True, on_delete=models.CASCADE)
	id_participante = models.ForeignKey(Participante2, verbose_name="Participante", null=True, blank=True, on_delete=models.CASCADE)
	nivel = models.CharField(max_length=10, null=True,verbose_name="Nivel")

	class Meta():
		verbose_name = "Atributo"
		verbose_name_plural = "Atributos"
		ordering = ["id"]

	def __str__(self):
		return self.id_estudiante.name

class LineaSemillero(models.Model):

	id = models.AutoField(primary_key=True, verbose_name="Id")
	id_coo = models.ForeignKey(Integrante, verbose_name="Coordinador", null=True, blank=True, on_delete=models.CASCADE)
	id_linea = models.ForeignKey(Linea,verbose_name="Id de la línea", null=True,on_delete=models.CASCADE)
	id_participante = models.ForeignKey(Participante2, verbose_name="Participante", null=True, blank=True, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True)
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)

	class Meta():
		verbose_name = "Línea por coordinador"
		verbose_name_plural = "Líneas por coordinador"
		ordering = ["-created"]

	def __str__(self):
		return self.id_coo.name

class coordinadores(models.Model):
	id = models.AutoField(primary_key=True, verbose_name="Id")
	Integrante = models.ForeignKey(Integrante, verbose_name="Integrante", null=True, blank=True, on_delete=models.CASCADE)
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	id_semillero = models.CharField(max_length=100, verbose_name="Semillero", null=True)

	class Meta():
		verbose_name = "Coordinador"
		verbose_name_plural = "Coordinadores"
		ordering = ["id"]

	def __str__(self):
		return self.user.username