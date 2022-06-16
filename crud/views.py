from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from crud.models import familiar

# Create your views here.
def inicio(request):

    familiares = familiar.objects.all()
    return render(request,"index.html", {'familiar':familiares})


def alta(request):
    
    nom = request.get['nombre']
    ape = request.get['apellido']
    nac = request.get['nacimiento']
    docu = request.get['dni']

    fam = familiar.objects.create(nombre=nom, apellido=ape, fecha_nacimiento=nac,
            dni=docu)

    return HttpResponse(response)
 

