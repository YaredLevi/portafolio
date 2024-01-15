from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def inicio_sesion(request):
    return render(request, 'registration/login.html')
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Registrado correctamente')
            return redirect(to="inicio")
        data['form'] = form

    return render(request, 'registration/registro.html',data)
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