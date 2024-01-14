from django.db import models


# Create your models here.

class Ticket(models.Model):
    descripcion = models.CharField(max_length=80)
    categoría = models.CharField(max_length=100, default='General')

    def __str__(self):
        return self.descripcion


class Evento(models.Model):
    nombre = models.CharField(max_length=80)
    fecha = models.DateField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='eventos', null=True)

    def __str__(self):
        return self.nombre
