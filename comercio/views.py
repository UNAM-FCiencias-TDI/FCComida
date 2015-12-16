from django.shortcuts import render,redirect
from .forms import ComercioForm
from django.contrib.auth.decorators import login_required

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
			# Guardamos el comercio en la base de datos
			form.save()
			#Esta linea y la anterior estaban mal identadas
			#Por eso moria con datos invalidos
			return redirect('comercio.views.exito')
		#Imprime los errores en el formulario
		else: 
			print form.errors

	else: 
		form = ComercioForm()

	return render(request,'comercio_registro.html', {'form': form})

# Creamos una vista de exito a alguna accion, este HTML no existe
def exito(request):
	return render(request, 'exito.html')



