from django.shortcuts import render,redirect
from .forms import ComercioForm


# Create your views here.

# Creamos la vista para registrar un comercio
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

		return redirect('comercio.views.exito')


	else: 
		form = ComercioForm()

	return render(request,'comercio_registro.html', {'form': form})

# Creamos una vista de exito a alguna accion
def exito(request):
	return render(request, 'exito.html')



