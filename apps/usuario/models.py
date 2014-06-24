from django.db import models
from django.contrib.auth.models import User

#Clase Usuario Rol
class UsuarioNormal(models.Model):
	usuario = models.OneToOneField(User)
	correo = models.CharField(max_length=100)
	pais = models.CharField(max_length=50)
	def __unicode__(self):
		return self.usuario.username
		

	#class Meta:
	#	abstract = True

#Clase UsuarioNormal
#class UsuarioNormal(models.Model):
#	correo = models.CharField(max_length=100)
#	pais = models.CharField(max_length=50)
#	
#	def __unicode__(self):
#		return self.correo
