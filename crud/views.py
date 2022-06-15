from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

from crud.models import Familiares

# Create your views here.
def inicio(request):

    familiares = Familiares.objects.all()
    nombre_completo = {'mi_nombre':'Ariel','mi_apellido':'Botti'}
    
    return render(request,"index.html", familiares)