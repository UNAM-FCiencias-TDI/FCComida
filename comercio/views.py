from django.shortcuts import render,redirect
from .forms import ComercioForm
from django.contrib.auth.decorators import login_required
from comercio.models import Comercio
from comentarios.models import Comentario
from django.contrib.auth.models import User
from perfiles.models import UserProfile
# Create your views here.

# Creamos la vista para registrar un comercio, solo usuarios con sesion iniciada
#Pueden registrar comercios, hay que manejar el error para cuando no lo estan
@login_required
def registro(request):
	# recibimos los datos por post
	if request.method == 'POST':
		
		form = ComercioForm(request.POST,request.FILES)

		if form.is_valid():

			# Vemos si se adjunto alguna foto del comercio
			if 'foto' in request.FILES:
				form.foto = request.FILES['foto']
			# Guardamos la informacion obtenida del formulario
			comercio = form.save(commit=False)
			# Asignamos el usuario logueado al comercio
			comercio.user = request.user
			# Guardamos el comercio en la base de datos
			comercio.save()
			return redirect('comercio.views.exito')
		#Imprime los errores en el formulario
		else: 
			print form.errors

	else: 
		form = ComercioForm()

	return render(request,'comercio_registro.html', {'form': form})

# Creamos una vista de exito a alguna accion, este HTML no existe
def exito(request):
	print request
	return render(request, 'exito.html')

def detalles_comercio(request, pk):
    detalles = Comercio.objects.get(pk=pk)
    #Obtenemos los comentarios que tengan el comercio como clave foranea
    try:
    	comentarios = Comentario.objects.filter(comercioId=pk)
    	print comentarios
    	perfiles = []
    	for comenta in comentarios:
    		perfiles.append(UserProfile.objects.get(pk=comenta.usuarioId.pk).picture)
    	print perfiles
    	print len(perfiles)
    	print len(comentarios)
    	comentarios = zip(comentarios, perfiles)
    except Comentario.DoesNotExist:
    	comentarios = None
    return render(request, 'detalles_comercio.html', {'comercio': detalles, 'comentarios':comentarios,})



