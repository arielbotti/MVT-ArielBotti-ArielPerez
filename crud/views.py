from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from crud.models import familiar

# Create your views here.
def inicio(request):

    familiares = familiar.objects.all()
    return render(request,"index.html", {'familiar':familiares})


def alta(request):
    
    nom = request.GET['nombre']
    ape = request.GET['apellido']
    nac = request.GET['nacimiento']
    docu = request.GET['dni']
    
    nuevo = familiar(nombre=nom, apellido= ape, fecha_nacimiento=nac, dni=docu)
    nuevo.save()

    #return HttpResponse(inicio)
    familiares = familiar.objects.all()
    return render(request,"index.html", {'familiar':familiares})

def borrar(request):



    familiares = familiar.objects.all()
    return render(request,"index.html", {'familiar':familiares})