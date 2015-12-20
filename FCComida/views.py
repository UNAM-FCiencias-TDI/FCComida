from django.http import HttpResponse
from django.shortcuts import render
from comercio.models import Comercio
def inicio(request):
	#Lista de los comercios a mostrar en el index (top 10), temporalmente se ordenan por el nombre
	lista_comercios = Comercio.objects.order_by('nombre')[:10]
	#Diccionario para iterar en el index
	comercios_dic = {'Comercios': lista_comercios}
	return render(request, 'home.html', comercios_dic)
def perfiles(request):
    return render(request, 'home.html')

