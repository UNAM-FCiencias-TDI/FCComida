from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Comercio(models.Model):
	
	#id  - ya la tiene por default, va tomando el mayor + 1 -es unica-
	nombre = models.CharField(max_length=50 ,default='')

	FACULTADES = (
    	('Facultad de Arquitectura', 'Facultad de Arquitectura'),
    	('Facultad de Derecho','Facultad de Derecho'),
    	('Facultad de Ciencias','Facultad de Ciencias'),
    	('Facultad de Ciencias Politicas y Sociales','Facultad de Ciencias Politicas y Sociales'),
    	('Facultad de Contaduria y Administracion','Facultad de Contaduria y Administracion'),
    	('Facultad de Economia','Facultad de Economia'),
    	('Facultad de Filosofia y Letras','Facultad de Filosofia y Letras'),
    	('Facultad de Ingenieria','Facultad de Ingenieria'),
    	('Facultad de Medicina','Facultad de Medicina'),
    	('Facultad de Quimica','Facultad de Quimica'),
    	('Facultad de Odontologia','Facultad de Odontologia'),
    	('Facultad de Psicologia','Facultad de Psicologia'),
    	('Facultad de Veterinaria y Zootecnia','Facultad de Veterinaria y Zootecnia'),
    )
	facultad = models.CharField(max_length=50, choices=FACULTADES ,default='')
	
	# un promedio de la calificacion
	calificacion = models.IntegerField( default = 0,
		validators=[MaxValueValidator(10),MinValueValidator(0)]
		) 

	comedor = models.BooleanField(default=True) #Cuenta o no con comedor

	# foto = models.BinaryField()
	foto = models.ImageField(upload_to='comercio_img/', blank=True)

	# ubicacion para maps
	latitud = models.DecimalField(
		max_digits=30, decimal_places=15, default = 19.3234728,
		validators=[MaxValueValidator(90.0),MinValueValidator(-90.0)]
		)
	longitud = models.DecimalField(
		max_digits=30, decimal_places=15, default=-99.1814817,
		validators=[MaxValueValidator(180.0),MinValueValidator(-180.0)]
		)
	
	# menor y mayor precio de los productos
	mayor_precio = models.FloatField(default=0.5, validators=[MinValueValidator(0.5)])
	menor_precio = models.FloatField(default=0.5, validators=[MinValueValidator(0.5)])
	
	descripcion = models.CharField(max_length=200, default='') # descripcion sobre el comercio
	#Se agrega el usuario y la fecha en la que lo registro
	fecha = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(User)

	'''Nos ayudara a visualizar mejor en shell'''
	def __str__(self):
		return str(self.id) + "Fac: " + self.facultad +  "Nombre: " + self.nombre