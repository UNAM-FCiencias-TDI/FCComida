from django.db import models

# Create your models here.
class Comercio(models.Model):
	"""docstring for Comercio"""
	idComercio = models.IntegerField(primary_key=True)
	calif = models.IntegerField()
	comedor = models.BinaryField()
	facultad = models.CharField(max_length=200)
	foto = models.ImageField()
	latitud = models.IntegerField()
	longitud = models.IntegerField()
	mayorPrecio = models.FloatField()
	menorPrecio = models.FloatField()
	nombre = models.CharField(max_length=100)
	recomendadaId = models.IntegerField()
	descripcion = models.CharField(max_length=240)

class Usuario(models.Model):
	idUsuario = models.IntegerField(primary_key=True)
	apellidoP = models.CharField(max_length=100)
	apellidoM = models.CharField(max_length=100)
	nombre = models.CharField(max_length=100)
	contrasenia = models.CharField(max_length=300)
	correo = models.EmailField(max_length=100)
	nombreUsuario = models.CharField(max_length=100)
	clss = models.BinaryField()

class Comida(models.Model):
	idComida = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=100)
	precio = models.IntegerField()
	tipo = models.CharField(max_length=200)
	comercioId = models.ForeignKey('Comercio')

class Comentario(models.Model):
	idComentario = models.IntegerField(primary_key=True)
	comentario = models.TextField()
	comercioId = models.ForeignKey('Comercio')
	fecha = models.DateTimeField()
	usuarioId = models.ForeignKey('Usuario')

class Calificacion(models.Model):
	idCalificacion = models.IntegerField(primary_key=True)
	calificacion = models.IntegerField()
	comercioId = models.ForeignKey('Comercio')
	usuarioId = models.ForeignKey('Usuario')