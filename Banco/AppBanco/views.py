from msilib.schema import ListView
from re import template
import tempfile
from django.shortcuts import render
from AppBanco.models import *
from django.views.generic import *

# Create your views here.


def listar (request):
    listarcli=Cliente.objects.all()
    return render (request,"index.html",{"lista_cli":listarcli})


class ListadoClientes(ListView):
    model=Cliente
    template_name="cliente.html"


class ListadoUsuario(ListView):
    model=Usuario
    template_name="usuario.html"


class ListadoLineas(ListView):
    model=Lineas_de_credito
    template_name="lineas.html"


class ListadoCreditos(ListView):
    model=Creditos
    template_name="creditos.html"

