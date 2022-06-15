from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

from crud.models import Familiares

# Create your views here.
def inicio(request):

    familiares = Familiares.objects.all()
    
    
    return render(request,"index.html", {'familia':familiares})