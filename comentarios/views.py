from django.shortcuts import render
from comentarios.models import Comentario
from comentarios.models import Califica
from comercio.models import Comercio
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Avg
# Create your views here.
@login_required
def Comentarios(request):
	if request.method == 'POST':
		#Tomamos los datos de los campos del formulario por su nombre
		comercio = request.POST.get('comercioId')
		comentario = request.POST.get('comentario')
		#Pedimos el usuario que mando el comentario
		usuarioId = request.user
		#Obtenemos el comerco con el id enviado
		comercioId = Comercio.objects.get(id=comercio)
		#Creamos el comentario, esta un poco rudimentario, tal vez luego lo haga con el forms
		comment = Comentario.objects.create(comentario=comentario,comercioId=comercioId,usuarioId=usuarioId)
		comment.save()
		#Regresamos al usuario a la pagina desde la que envio el formulario, en este caso la del comercio
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
	else:
		#Con get lo mando a otro lado, no se si sea lo mejor
		return render(request, 'login.html', {})
#Analogo al anterior
@login_required
def Calificaciones(request):
	if request.method == 'POST':
		comercio = request.POST.get('comercioId')
		califica = request.POST.get('rating')
		usuarioId = request.user
		comercioId = Comercio.objects.get(id=comercio)
		valores_actualiza = {'califica':califica}
		#Si el usuario no ha calificado ese comercio se crea una nueva entrada en la base,
		#si ya lo califico solo se actualiza su puntuacion, esto evita calificar multiples veces
		calif, created = Califica.objects.update_or_create(
			comercioId=comercioId,usuarioId=usuarioId,defaults=valores_actualiza)
		#obtenemos el conjunto de calificaciones del comericio
		prom = Califica.objects.filter(comercioId=comercioId)
		#calculamos el promedio y lo guardamos como entero
		promedio = int (round (prom.aggregate(Avg('califica'))['califica__avg']))
		#Obtenemos el comercio calificado
		detalles = Comercio.objects.get(pk=comercio)
		#Guardamos el promedio en el comercio
		detalles.calificacion = promedio
		#Guardamos el comercio
		detalles.save()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
	else:
		return render(request, 'login.html', {})
