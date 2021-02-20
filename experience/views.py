from django.shortcuts import render
from .models import *
# Create your views here.

def sobreMi(request):
    tecno = Lenguajes.objects.order_by('lenguaje')
    experi = Experience.objects.all()

    return render(request, 'sobreMi.html', {
        'tecnologias': tecno,
        'experiencias': experi
    })
#end sobreMi