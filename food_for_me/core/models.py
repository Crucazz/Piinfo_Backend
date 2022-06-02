from django.db import models

from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class User(AbstractUser):
	email=models.EmailField(unique=True)
	telefono = models.CharField(max_length=12, null=True)
	edad=models.IntegerField(null=True)
	suscripcion=models.DateTimeField(null=True)

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
	def authenticate(self, request, username=None, password=None, **kwargs):
		UserModel=get_user_model()		
		try:
			user = UserModel.objects.get(username=username)
		except UserModel.DoesNotExist:
			try:
				user = UserModel.objects.get(email=username)
			except UserModel.DoesNotExist:
				UserModel().set_password(password)
			else:
				if user.check_password(password) and self.user_can_authenticate(user):
					return user
		else:
			if user.check_password(password) and self.user_can_authenticate(user):
				return user

		
		

		pass


class Restriccion(models.Model):
	tipo = models.IntegerField()
	descripcion = models.CharField(max_length=300)
	def _str_(self):
		return self.tipo

class Usuario_Restriccion(models.Model):
	usuario = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
	restriccion = models.ForeignKey(Restriccion, to_field='id', on_delete=models.CASCADE)

class Producto(models.Model):
	nombre = models.CharField(max_length=100)
	categoria = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=500)
	imagen = models.CharField(max_length=500)
	image = models.ImageField()
	def _str_(self):
		return self.nombre

class Pyme(models.Model):
	nombre = models.CharField(max_length=100)
	telefono = models.CharField(max_length=10)
	correo = models.CharField(max_length=500)
	sitio_web = models.CharField(max_length=500)
	def _str_(self):
		return self.nombre

class Propaganda(models.Model):
	nombre_producto = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=500)
	pyme = models.ForeignKey(Pyme, to_field='id', on_delete=models.CASCADE)
	def _str_(self):
		return self.nombre_producto