from django.shortcuts import render
from .formulario import ContactForm
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
"""
def holaMundo(request):

    return render(request, 'index.html', {})
#End holaMundo
"""
def main_view(request):

    return render(request, 'main.html', {})
#End main_view

def main_contacto(request):
    formulario = ContactForm()

    if request.method == 'POST':
        asunto = 'Contacto desde formulario de web'
        mensaje = "De: " + request.POST['correo']
        mensaje = mensaje + "\nTeléfono: " + request.POST['telefono']
        mensaje = mensaje + "\nMensaje:\n" + request.POST['mensaje']
        de_ = 'formyaredblog@gmail.com'
        para_ = 'yareddeltoro@gmail.com'

        respuesta = send_mail(asunto, mensaje, de_, [para_] , fail_silently=False)
        if respuesta == 1:
            messages.success(request, 'Mensaje enviado correctamente')
        elif respuesta == 0:
            messages.success(request, 'Hubo un error, intente de nuevo')
        #Endif
    #End if

    return render(request, 'contacto.html', {
        'form':formulario,
    })
#End main_contacto