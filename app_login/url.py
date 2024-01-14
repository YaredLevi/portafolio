from django.urls import path
from . import views


#URLS APP LOGIN
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('iniciar-sesion', views.inicio_sesion, name='inicio_sesion'),
    path('registro', views.registro, name='registro'),
    path('solicitud', views.solicitud, name='solicitud')

]