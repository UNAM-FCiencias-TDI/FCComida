from django.http import HttpResponse
from django.shortcuts import render
def inicio(request):
    return render(request, 'home.html')
def perfiles(request):
    return render(request, 'home.html')


