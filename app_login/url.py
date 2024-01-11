from django.urls import path
from . import views


#URLS APP LOGIN
urlpatterns = [
    path('', views.index)
]