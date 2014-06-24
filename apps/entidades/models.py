from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

#Clase Evento
class Evento(models.Model):
	idEvento = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=200)
	propietario = models.ForeignKey(User)
	class Meta:
		abstract = True

class NotaRapida(Evento):
	def __unicode__(self):
		return self.nombre
		
class Tarea(Evento):
	fecha = models.DateTimeField('date published')
	def __unicode__(self):
		return self.nombre
	class Meta:
		ordering = ["-fecha"]
		
class Lugar(models.Model):
	nombre = models.CharField(max_length=100)
	lat = models.CharField(max_length=50)
	lon = models.CharField(max_length=50)
	def __unicode__(self):
		return self.nombre 
		
class LugarForm(ModelForm):
	class Meta:
		model = Lugar
		
class EventoSocial(Evento):
	fecha = models.DateTimeField('date published')
	lugar = models.OneToOneField(Lugar)
	invitados = models.ManyToManyField(User, related_name = 'invitados', blank = True)
	def __unicode__(self):
		return self.nombre
	class Meta:
		ordering = ["-fecha"]


	
