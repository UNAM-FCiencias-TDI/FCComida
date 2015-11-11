from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from comercio.models import Comercio
from usuarios.models import Usuario
# Create your models here.
class Comentario(models.Model):
	comentario = models.TextField()
	comercioId = models.ForeignKey(Comercio)
	fecha = models.DateTimeField(auto_now_add = True)
	usuarioId = models.ForeignKey(Usuario)

class Califica (models.Model):
	califica = models.PositiveIntegerField(
		validators=[MaxValueValidator(10), MinValueValidator(1)]
		)
	comercioId = models.ForeignKey(Comercio)
	usuarioId = models.ForeignKey(Usuario)
