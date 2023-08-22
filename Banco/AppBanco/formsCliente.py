from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta: 
        model = Cliente
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'direccion', 'genero']