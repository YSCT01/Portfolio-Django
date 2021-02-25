from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def proyectos(request):
    projects = Proyecto.objects.all().order_by('proyecto')

    return render(request, 'proyectos.html', {
        'proyectos':projects,
    })

def proyecto(request, id):
    proyect = get_object_or_404(Proyecto, id=id)

    return render(request, 'proyecto.html', {
        'proyecto':proyect,
    })
#end proyectos