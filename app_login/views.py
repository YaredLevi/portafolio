from django.shortcuts import render
from .models import Evento
from django.http import HttpResponse
# Create your views here.

def inicio_sesion(request):
    return render(request, 'inicio_sesion.html')
def registro(request):
    return render(request, 'registro.html')
def inicio(request):
    #lista las instancias de la entidad evento
    #luego saldran en inicio
    eventos = Evento.objects.all()

    #debe ser diccionario para admintir los atributos
    data = {
        "eventos": eventos
    }

    return render(request, 'inicio.html', data)
def solicitud(request):
    return render(request, 'solicitud.html')