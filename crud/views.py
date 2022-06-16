from django.shortcuts import render
from crud.models import familiar

# Create your views here.
def inicio(request):

    familiares = familiar.objects.all()
    return render(request,"index.html", {'familiar':familiares})