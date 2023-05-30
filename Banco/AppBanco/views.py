from ast import Try
from atexit import register
from pydoc import cli
from django.shortcuts import render
from AppBanco.models import *
from django.views.generic import *
from django.http import *
from django.utils.decorators import *
from django.views.decorators.csrf import *
import json


# Create your views here.


""" def listar (request):
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
    template_name="creditos.html" """



class ListadoClientes(View):
    def get(self,request):
        datos:Cliente.objects.all().values()
        datoscli=list(datos)
        return JsonResponse(datoscli,safe=False)


class InsertarCliente(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self,request):
        datos=json.loads(request.body)
        request.POST.GET('documento')
        request.POST.GET('nombre')
        request.POST.GET('apellido')
        request.POST.GET('correo')
        request.POST.GET('telefono')
        request.POST.GET('direccion')
        request.POST.GET('genero')

        cli=Cliente.objects.create(documento=datos['documento'],nombre=datos['nombre'],apellido=datos['apellido'],correo=datos['correo'],telefono=datos['telefono'],direccion=datos['direccion'],genero=datos['genero'],)
        cli.save()
        return JsonResponse({'mensaje':'datos guardados'})


class ActualizarCliente(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def put(self,request,pk):
        try:
            registro=Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return JsonResponse({"error":"el documento no exoste"})
        data=json.loads(request.body)
        registro.nombre=data.get('nombre')
        registro.nombre=data.get('apellido')
        registro.nombre=data.get('correo')
        registro.nombre=data.get('telefono')
        registro.nombre=data.get('direccion')
        registro.nombre=data.get('genero')
        registro.save()
        return JsonResponse({'Mensaje':'datos actualizados'})



class Eliminar(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self,request,pk):
        try:
            registro=Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return JsonResponse({"error":"el documento no exoste"})
        
        registro.delete()
        return JsonResponse({'mensaje':'dato eliminado'})


















































