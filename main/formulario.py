from django import forms
from django.core import validators

class ContactForm(forms.Form):
    nombre = forms.CharField(
        label="Escribe tu nombre* ",
        min_length=3,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Nombre',
                'class':'textoForm'
            }
        ),
        validators=[
            validators.MinLengthValidator(5, 'Escribe tu nombre completo'),
        ]
    )

    telefono = forms.CharField(
        label='Escribe tu teléfono* ',
        min_length=10,
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Número de teléfono',
                'class':'textoForm'
            }
        ),
        validators=[
            validators.MinLengthValidator(5, 'Escribe tu número de teléfono a 10 dígitos')
        ]
    )

    correo = forms.CharField(
        label="Escribe tu correo electrónico* ",
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Correo electrónico',
                'class':'textoForm',
                'type':'email'
            }
        ),
        validators=[
            validators.EmailValidator()
        ]
    )

    mensaje = forms.CharField(
        label='Escribe tu mensaje* ',
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder':'Escribe tu mensaje',
                'class':'textareaForm',
            }
        )
    )
#End ContactForm