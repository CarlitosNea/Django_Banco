
from atexit import register
from pydoc import cli
from django.shortcuts import render
from AppBanco.models import *
from django.views.generic import *
from django.http import *
from django.utils.decorators import *
from django.views.decorators.csrf import *
import json
from django.contrib.auth.decorators import *


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
        datos=Cliente.objects.all().values()
        datoscli=list(datos)
        return render(request,'cliente.html',{'datos':datoscli})


class InsertarCliente(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    """ @method_decorator(login_required) """
    def post(self,request):
    
        try: 
            datos=json.loads(request.body)
        except(json.JSONDecodeError,UnicodeDecodeError):
            return JsonResponse({"error":"error :("})
        Documento=datos.get('documento')
        Nombre=datos.get('nombre')
        Apellido=datos.get('apellido')
        Correo=datos.get('correo')
        Telefono=datos.get('telefono')
        Direccion=datos.get('direccion')
        Genero=datos.get('genero')
        cli=Cliente.objects.create(documento=Documento,nombre=Nombre,apellido=Apellido,correo=Correo,telefono=Telefono,direccion=Direccion,genero=Genero,)
        cli.save()
        """ return render(request,'form.html',{'mensaje':'Datos guardados'}) """
        return JsonResponse({"mensaje":"datos guardaros"})

class ActualizarCliente(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def put(self,request,pk):
        try:
            registro=Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return JsonResponse({"error":"el documento no existe"})
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
    




def formularioInsertar(request):
    return render(request,"form.html")        