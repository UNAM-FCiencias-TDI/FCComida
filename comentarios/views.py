from django.shortcuts import render
from comentarios.models import Comentario
from comercio.models import Comercio
from django.http import HttpResponseRedirect
# Create your views here.
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