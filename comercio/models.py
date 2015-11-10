from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Comercio(models.Model):
	#id  - ya la tiene por default, va tomando el mayor + 1 -es unica-
	calificacion = models.PositiveIntegerField(
		validators=[MaxValueValidator(10),MinValueValidator(1)]
		)
	comedor = models.BooleanField()
	facultad = models.CharField(max_length=200)
	nombre = models.CharField(max_length=100)
	foto = models.BinaryField() #ImageField()
	latitud = models.DecimalField(
		max_digits=5, decimal_places=3,
		validators=[MaxValueValidator(90.0),MinValueValidator(-90.0)]
		)
	longitud = models.DecimalField(
		max_digits=5, decimal_places=3,
		validators=[MaxValueValidator(180.0),MinValueValidator(-180.0)]
		)
	mayor_precio = models.FloatField(validators=[MinValueValidator(0.5)])
	menor_precio = models.FloatField(validators=[MinValueValidator(0.5)])
	#recomendada_id 
	#descripcion

	'''Nos ayudara a visualizar mejor en shell'''
	def __str__(self):
		return str(self.id) + "Fac: " + self.facultad +  "Nombre: " + self.nombre