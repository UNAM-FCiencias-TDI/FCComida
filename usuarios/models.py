from django.db import models

# Create your models here.
class Usuario(models.Model):
	#idUsuario = models.IntegerField(primary_key=True)
	apellidoP = models.CharField(max_length=100)
	apellidoM = models.CharField(max_length=100)
	nombre = models.CharField(max_length=100)
	contrasenia = models.CharField(max_length=300)
	correo = models.EmailField(max_length=100)
	nombreUsuario = models.CharField(max_length=100)
	clss = models.BooleanField()
