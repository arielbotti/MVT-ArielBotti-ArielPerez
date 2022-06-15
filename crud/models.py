from django.db import models
from django.forms import CharField, DateField


class Familiares(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField(blank=True)
    dni = models.IntegerField(unique=True)